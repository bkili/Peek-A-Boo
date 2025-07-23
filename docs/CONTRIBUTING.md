# Development & Testing Workflow

To maintain high code quality and prevent regressions, all developers are expected to run checks before committing any changes.

## Pre-Commit Check Script

Before making a commit, run the following command from the project root:

```
./tools/check_before_commit.sh
```

### This script performs:

- Code Formatting & Linting: 
  - Runs black and flake8 on all Python files, using the configuration defined in tools/.pre-commit-config.yaml and tools/.flake8.
	

- Unit Tests: 
  - Runs pytest with coverage for the core/ and modules/ directories.

**If any check fails, the commit will be blocked. Please fix the issues and rerun the script before sending PR.**

## Project Layout for Dev Tools

**The following files are located in the tools/ directory:**

- .pre-commit-config.yaml — Pre-commit hook configuration
- .flake8 — Linter settings
- check_before_commit.sh — Main check runner (lint + test)
- precommit_pytest.sh — Used internally to run tests with coverage

_Note: These tools are for development only and not packaged in production builds. You may move them or replace them with a Makefile in the future._

### Example Output

[ * ] Running code format & lint checks via pre-commit...
```
black....................................................................Passed

flake8...................................................................Passed

[ * ] Running unit tests with pytest...

[ ✓ ] All checks passed. Ready to commit!
```

If errors are found, you will see a detailed report with line numbers and messages (e.g., for flake8 violations or test failures).

---