#!/bin/bash

# Create requirements directory if it doesn't exist
mkdir -p requirements

# Generate main requirements.txt with hashes
uv pip compile pyproject.toml \
    --generate-hashes \
    --output-file requirements/requirements.txt

# Generate development requirements
uv pip compile pyproject.toml \
    --generate-hashes \
    --output-file requirements/requirements-dev.txt \
    --extra dev

# Generate documentation requirements
uv pip compile pyproject.toml \
    --generate-hashes \
    --output-file requirements/requirements-docs.txt \
    --extra docs

# Generate all requirements (main + dev + docs)
uv pip compile pyproject.toml \
    --generate-hashes \
    --output-file requirements/requirements-all.txt \
    --extra dev --extra docs

echo "✅ Generated requirements files in requirements/ directory" 