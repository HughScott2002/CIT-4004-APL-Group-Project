# TypeSnake

A statically-typed, functional programming language that transpiles to Python.

Originally a university group project (CIT-4004) with a custom syntax (`scribe`, `hail`, `lock`/`unlock`, `attempt`/`findout`). The transpiler uses PLY for lexing and parsing, performs semantic analysis with scoped symbol tables, and generates executable Python.

> **Warning:** This is an experimental student project built for a university course (CIT-4004). It is not production software. The codebase has known issues (zero tests, `exec()` in the API, no type hints) and is maintained on a best-effort basis. For the long-term vision and how to contribute ideas, see [docs/FUTURE.md](docs/FUTURE.md) — PRs and suggestions are welcome.

## Authors

- Hugh Scott
- Barrington Patterson
- Sharethia McCarthy
- Christina Wilson

## Project Structure

```
.
├── src/typesnake/          Compiler core (lexer, parser, analyzer, codegen)
├── server/                 Flask API and CLI entry points
├── examples/               Sample TypeSnake source programs
├── docs/                   Documentation, BNF grammar, future vision
├── tests/                  Test suite (scaffolded)
├── flake.nix                Nix flake (dev shell with `nix develop`)
├── pyproject.toml           Project metadata, ruff config
├── Dockerfile               Containerised deployment
├── compose.yaml             Docker Compose configuration
└── requirements.txt         Python dependencies
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask API server
PYTHONPATH=src python server/main.py

# Or via gunicorn
PYTHONPATH=src gunicorn --bind=0.0.0.0 --timeout 600 server.main:app

# Run the CLI version
PYTHONPATH=src python server/app.py
```

## Nix

If you have Nix with flakes enabled, one command gets you a shell with Python 3.12, all dependencies, ruff, and pytest:

```bash
nix develop
```

Inside the shell, `PYTHONPATH` is set automatically, so you can run directly:

```bash
python server/main.py       # API server
python server/app.py        # CLI
ruff check src/ server/     # lint
pytest                      # tests
```

Non-flake Nix: `nix-shell` also works via the included `shell.nix`.

## Docker

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

## Resources

- [TypeSnake Documentation](https://docs.google.com/document/d/1HaJzZFqHK1ZdScXy_jM797ikMFCdwXuMlkATgj-Xj2U/edit?usp=sharing)
- [TypeSnake Website](https://apl-web-ui.vercel.app/)

## Future Direction

This project is exploring a transition to a Python superset with mandatory type annotations, additional syntax sugar, and a `tsnake` CLI for project scaffolding, running, and building. See [docs/FUTURE.md](docs/FUTURE.md).
