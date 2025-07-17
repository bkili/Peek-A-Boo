# Peek-A-Boo

Peek-A-Boo is a modular and extensible post-exploitation framework focused on offensive security operations, including OSINT, exploitation, and privilege escalation. Designed with flexibility in mind, it allows users to easily create, extend, and control their own tooling from a unified CLI interface.

## Features

- Modular architecture (modules, exploits, shared runtime)
- Easily extensible — write and integrate your own tools
- CLI interface with autocompletion and intelligent command handling
- Configuration persistence with `config save <name>` and `config load <name>`
- Shared runtime data (`shared_data`) for communication between modules
- Run modules independently or as chained operations
- Full control over local or custom exploits and payloads
- Supports multiple module categories (recon, privilege_escalation, osint, utility)
- Developer-friendly plugin structure with `BaseModule` inheritance
- Colored CLI output using `rich` formatting via `printc()`

## Requirements

- Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Example commands:

```bash
list modules
use pb_scrape_keywords
run

save config target1
load config target1
```

## Directory Structure

```
Peek-A-Boo/
├── core/                 # Core framework (CLI, state, registry, utils)
   └── utils/             # Reusable utility modules (formatter, ssh_handler, etc.)
├── modules/              # Modules: osint, recon, privilege escalation, utility, etc.
├── exploits/             # Exploits and payload logic (CVE-style or custom)
├── main.py               # CLI entry point
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── docs                  # Documentations, Images etc.
   └── DEVELOPER_GUIDE.md # Developer guide for writing modules
```

## Shared Data System

Modules can optionally write to or read from a shared runtime dictionary (`shared_data`) allowing chained operations or collaborative logic between tools. Modules can operate:

- Standalone (fully independent)
- Interdependent (reading results from others using `shared_data.get("key")`)

This enables seamless chaining like OSINT → Recon → Exploitation, while maintaining modular separation.

## Module Types

- `modules/`: Tools or tasks (e.g., recon, OSINT, privilege escalation)
- `exploits/`: Local/remote code execution components or payloads
- Each module should inherit from `BaseModule` and define:
  - `run(self, shared_data)`
  - `requires(self)`
  - Metadata fields (`name`, `category`, etc.)

## Configuration System

Save and load your settings with ease:

```bash
config save mysetup
config load mysetup
```


## Disclaimer

This project is intended for educational and authorized security research. Do not use on systems without explicit permission.


## For Developers

For implementation details, module structure, and extension guidelines, please refer to the [Developer Guide](docs/DEVELOPER_GUIDE.md).