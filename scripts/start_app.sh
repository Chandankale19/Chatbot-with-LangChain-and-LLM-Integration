#!/bin/bash
set -e

echo "Starting application..."
source venv/bin/activate
uvicorn src.app:app --host 0.0.0.0 --port 8000