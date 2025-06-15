#!/usr/bin/env bash
set -euxo pipefail

# uv run fastapi dev main.py

uv run fastapi dev --host 0.0.0.0 --port 16888 main.py

# uv run fastapi dev --help