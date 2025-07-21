## Core Improvements

- [ ] Refactor `core/cli.py` for better modularity and input validation.
- [ ] Implement logging configuration system (`core/logging.py`).
- [ ] Add persistent session state saving and restoration.
- [ ] Improve exception handling across all core command handlers.
- [ ] Add support for custom command aliases.
- [ ] Implement a command history feature with search capabilities.
- [ ] Add global settings management (e.g. `config.json`).

## Modules & Plugins

- [ ] Add real-world CVE module: CVE-2021-4034 (pkexec).
- [ ] Add CVE-2023-25136 OpenSSH vulnerability module.
- [ ] Add Windows privilege escalation module using DLL hijacking.
- [ ] Add Linux kernel local exploit module (e.g. DirtyPipe or DirtyCow).
- [ ] Design plugin architecture documentation and examples.

## Exploits

- [ ] Refactor existing `exp_cve_2025_32463` to be fully config-agnostic.
- [x] ~~Add module dependency checker before running exploits.~~
- [ ] Add optional post-exploitation plugin support.

## Tests

- [ ] Add integration tests with a fake SSH server (e.g. `paramiko.ServerInterface`).
- [x] ~~Add integration tests for cli commands.~~
- [ ] Add CLI history and command replay tests.
- [x] ~~Mock file-based config loading and saving in `test_config_ops.py`.~~
- [ ] Add unit test for `core/commands/module_ops.py`.
- [x] ~~Test error propagation for missing module options in `run()`.~~

## GitHub Actions & CI/CD

- [x] ~~Add test matrix for Python 3.9, 3.10, 3.11 on Ubuntu, macOS, and Windows.~~
- [ ] Cache virtualenv between CI runs.
- [x] ~~Upload test coverage reports.~~
- [x] ~~Add `lint` job using `ruff` and/or `black`.~~

## Documentation

- [ ] Finalize `docs/DEVELOPER_GUIDE.md` with testing and contribution notes.
- [ ] Create architecture diagram (core, modules, CLI flow).
- [ ] Add sample `config.json` to `docs/` for demonstration.
- [x] ~~Document custom module creation process.~~

## CLI Enhancements

- [ ] Add `history` command to review previous inputs.
- [ ] Add `alias` system for frequently used commands.
- [x] ~~Improve `set` command with auto-completion for option names.~~
- [x] ~~Add `reload` command to reload current module without restarting CLI.~~

## Optional Features

- [ ] Add `peek-scan` command line mode for one-shot scanning.
- [ ] Create plugin marketplace directory on GitHub.
- [ ] Provide `setup.py` or `pyproject.toml` for package installation.
