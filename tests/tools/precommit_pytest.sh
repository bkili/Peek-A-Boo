#!/bin/bash
set -e

echo "[*] Running pytest with coverage inside pre-commit hook..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

# Activate .venv if needed
if [ -d "$PROJECT_ROOT/.venv" ]; then
    source "$PROJECT_ROOT/.venv/bin/activate"
fi

PYTHONPATH="$PROJECT_ROOT" pytest --quiet --tb=short "$PROJECT_ROOT/tests"

echo "[✓] Pytest completed successfully."