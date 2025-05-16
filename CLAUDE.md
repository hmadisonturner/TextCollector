# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands
- Install: `pip install -r requirements.txt`
- Run app: `python -m text_collector [options]`
- Run all tests: `pytest`
- Run specific test: `pytest tests/test_file.py::test_function_name`
- Run with coverage: `pytest --cov=.`

## Code Style Guidelines
- Follow Google Python Style Guide
- Imports: standard library first, third-party packages second, relative imports last
- Use docstrings for all functions in Google style format
- Function naming: verb_noun format with snake_case
- Error handling: Use specific exceptions with informative error messages
- Typing: Document types in docstrings
- Prefer modular architecture with separation of concerns

Before submitting changes:
- Run all tests
- Ensure code follows existing patterns in the repo
- Document all new parameters in both docstrings and CLI help text
