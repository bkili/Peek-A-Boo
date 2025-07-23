#!/bin/bash

echo "[*] Running code format & lint checks via pre-commit..."
if ! pre-commit run --config tests/tools/.pre-commit-config.yaml --all-files; then
  echo "[!] Pre-commit checks failed. Please fix the issues and retry."
  exit 1
fi

echo "[*] Running unit tests with pytest..."
PYTHONPATH=$(pwd)
if ! PYTHONPATH=$(pwd) pytest tests; then
  echo "[!] Unit tests failed. Please fix the errors before committing."
  exit 1
fi

echo "[✓] All checks passed. Ready to commit!"