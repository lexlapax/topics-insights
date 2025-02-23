"""
Setup script for Supabase database schema and functions.
"""
from supabase import create_client, Client
from typing import List

SCHEMA_SQL = """
-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "vector";

-- Create tables
CREATE TABLE IF NOT EXISTS topics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    description TEXT,
    keywords TEXT[] NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    user_id UUID REFERENCES auth.users(id),
    is_active BOOLEAN DEFAULT true,
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS summaries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    source_url TEXT,
    source_type TEXT,
    sentiment TEXT,
    key_concepts TEXT[]
);

CREATE TABLE IF NOT EXISTS topic_embeddings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE,
    embedding vector(1536),
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_topics_keywords ON topics USING GIN (keywords);
CREATE INDEX IF NOT EXISTS idx_topics_metadata ON topics USING GIN (metadata);
CREATE INDEX IF NOT EXISTS idx_summaries_topic_id ON summaries(topic_id);
CREATE INDEX IF NOT EXISTS idx_summaries_created_at ON summaries(created_at);
CREATE INDEX IF NOT EXISTS idx_topic_embeddings_topic_id ON topic_embeddings(topic_id);
CREATE INDEX IF NOT EXISTS idx_topic_embeddings_embedding ON topic_embeddings USING ivfflat (embedding vector_cosine_ops);

-- Create functions
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION store_embeddings(
    p_topic_id UUID,
    p_embedding vector,
    p_metadata jsonb DEFAULT '{}'::jsonb
) RETURNS UUID AS $$
DECLARE
    v_embedding_id UUID;
BEGIN
    INSERT INTO topic_embeddings (topic_id, embedding, metadata)
    VALUES (p_topic_id, p_embedding, p_metadata)
    RETURNING id INTO v_embedding_id;
    
    RETURN v_embedding_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION search_similar_content(
    query_embedding vector,
    similarity_threshold float DEFAULT 0.8,
    match_count int DEFAULT 10
) RETURNS TABLE (
    topic_id UUID,
    similarity float,
    metadata jsonb
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        e.topic_id,
        1 - (e.embedding <=> query_embedding) as similarity,
        e.metadata
    FROM topic_embeddings e
    WHERE 1 - (e.embedding <=> query_embedding) > similarity_threshold
    ORDER BY similarity DESC
    LIMIT match_count;
END;
$$ LANGUAGE plpgsql;

-- Create triggers
CREATE TRIGGER update_topics_updated_at
    BEFORE UPDATE ON topics
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();

-- Create RLS policies
ALTER TABLE topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE summaries ENABLE ROW LEVEL SECURITY;
ALTER TABLE topic_embeddings ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read their own topics"
    ON topics FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own topics"
    ON topics FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own topics"
    ON topics FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own topics"
    ON topics FOR DELETE
    USING (auth.uid() = user_id);

-- Similar policies for summaries and embeddings
"""

FUNCTIONS_SQL = """
-- Additional utility functions
CREATE OR REPLACE FUNCTION get_topic_summary(
    p_topic_id UUID,
    p_days_back integer DEFAULT 7
) RETURNS TABLE (
    summary_text TEXT,
    key_concepts TEXT[],
    sentiment TEXT,
    source_count integer
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        string_agg(s.content, E'\n\n' ORDER BY s.created_at DESC) as summary_text,
        array_agg(DISTINCT unnest(s.key_concepts)) as key_concepts,
        mode() WITHIN GROUP (ORDER BY s.sentiment) as sentiment,
        count(DISTINCT s.source_url) as source_count
    FROM summaries s
    WHERE s.topic_id = p_topic_id
    AND s.created_at >= NOW() - (p_days_back || ' days')::interval;
END;
$$ LANGUAGE plpgsql;
"""

async def setup_database(client: Client):
    """Setup the Supabase database schema and functions."""
    try:
        # Execute schema SQL
        await client.postgrest.connection().execute(SCHEMA_SQL)
        print("✅ Schema created successfully")

        # Execute functions SQL
        await client.postgrest.connection().execute(FUNCTIONS_SQL)
        print("✅ Functions created successfully")

    except Exception as e:
        print(f"❌ Error setting up database: {str(e)}")
        raise

if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    import os

    load_dotenv()

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not all([supabase_url, supabase_key]):
        raise ValueError("Missing Supabase credentials")

    client = create_client(supabase_url, supabase_key)
    asyncio.run(setup_database(client)) 