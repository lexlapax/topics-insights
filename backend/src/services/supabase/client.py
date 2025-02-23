"""
Supabase client service for database operations and real-time subscriptions.
"""
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from functools import lru_cache

from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions
from pydantic import BaseModel

class SupabaseConfig(BaseModel):
    url: str
    key: str
    timeout: int = 30
    schema: str = "public"
    auto_refresh_token: bool = True
    persist_session: bool = True

class SupabaseService:
    def __init__(self, config: SupabaseConfig):
        options = ClientOptions(
            schema=config.schema,
            auto_refresh_token=config.auto_refresh_token,
            persist_session=config.persist_session,
            timeout=config.timeout
        )
        self.client: Client = create_client(config.url, config.key, options)
        self._setup_realtime_subscriptions()

    def _setup_realtime_subscriptions(self):
        """Setup realtime subscriptions for relevant tables."""
        self.client.table('topics').on('*', self._handle_topic_changes).subscribe()
        self.client.table('summaries').on('*', self._handle_summary_changes).subscribe()

    async def _handle_topic_changes(self, payload):
        """Handle real-time topic changes."""
        # Implementation for real-time updates

    async def _handle_summary_changes(self, payload):
        """Handle real-time summary changes."""
        # Implementation for real-time updates

    # Topic Operations
    async def create_topic(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new topic with validation."""
        return await self.client.table('topics').insert(data).execute()

    async def get_topic(self, topic_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a topic by ID."""
        response = await self.client.table('topics')\
            .select('*, summaries(*)')\
            .eq('id', topic_id)\
            .single()\
            .execute()
        return response.data if response else None

    async def update_topic(self, topic_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a topic."""
        return await self.client.table('topics')\
            .update(data)\
            .eq('id', topic_id)\
            .execute()

    async def delete_topic(self, topic_id: int) -> None:
        """Delete a topic and its related data."""
        async with self.client.postgrest.connection() as conn:
            await conn.execute("""
                BEGIN;
                DELETE FROM topic_embeddings WHERE topic_id = $1;
                DELETE FROM summaries WHERE topic_id = $1;
                DELETE FROM topics WHERE id = $1;
                COMMIT;
            """, topic_id)

    # Vector Operations
    async def store_embeddings(
        self, 
        topic_id: int, 
        embeddings: List[float],
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Store embeddings with metadata."""
        return await self.client.rpc(
            'store_embeddings',
            {
                'p_topic_id': topic_id,
                'p_embedding': embeddings,
                'p_metadata': metadata
            }
        ).execute()

    async def search_similar(
        self, 
        embedding: List[float],
        limit: int = 10,
        threshold: float = 0.8
    ) -> List[Dict[str, Any]]:
        """Search for similar content using vector similarity."""
        return await self.client.rpc(
            'search_similar_content',
            {
                'query_embedding': embedding,
                'similarity_threshold': threshold,
                'match_count': limit
            }
        ).execute()

    # Summary Operations
    async def create_summary(
        self,
        topic_id: int,
        content: str,
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Create a new summary with metadata."""
        data = {
            'topic_id': topic_id,
            'content': content,
            'metadata': metadata,
            'created_at': datetime.utcnow().isoformat()
        }
        return await self.client.table('summaries').insert(data).execute()

    async def get_topic_summaries(
        self,
        topic_id: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Get summaries for a topic with optional date range."""
        query = self.client.table('summaries')\
            .select('*')\
            .eq('topic_id', topic_id)\
            .order('created_at', desc=True)\
            .limit(limit)

        if start_date:
            query = query.gte('created_at', start_date.isoformat())
        if end_date:
            query = query.lte('created_at', end_date.isoformat())

        response = await query.execute()
        return response.data if response else []

    # Batch Operations
    async def batch_create_summaries(
        self,
        summaries: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Batch create summaries for better performance."""
        return await self.client.table('summaries')\
            .insert(summaries)\
            .execute()

    # Cache Operations
    @lru_cache(maxsize=1000)
    async def get_cached_topic(self, topic_id: int) -> Optional[Dict[str, Any]]:
        """Get topic with caching for better performance."""
        return await self.get_topic(topic_id)

    # Search Operations
    async def search_topics(
        self,
        query: str,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Search topics with filters."""
        search_query = self.client.table('topics')\
            .select('*')\
            .textSearch('name', query)\
            .limit(limit)

        if filters:
            for key, value in filters.items():
                search_query = search_query.eq(key, value)

        response = await search_query.execute()
        return response.data if response else []

    # Utility Methods
    async def health_check(self) -> bool:
        """Check database connection health."""
        try:
            await self.client.table('topics').select('id').limit(1).execute()
            return True
        except Exception:
            return False

    async def cleanup_old_data(self, days: int = 30) -> None:
        """Clean up old data to maintain performance."""
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        await self.client.table('summaries')\
            .delete()\
            .lt('created_at', cutoff_date.isoformat())\
            .execute() 