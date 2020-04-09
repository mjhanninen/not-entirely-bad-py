#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"
exec "$PROJECT_DIR/scripts/with-venv.sh" jupyter notebook --notebook-dir="$PROJECT_DIR/notebooks"
