# TypeSnake

A statically-typed, functional programming language that transpiles to Python.

Originally a university group project (CIT-4004) with a custom syntax (`scribe`, `hail`, `lock`/`unlock`, `attempt`/`findout`). The transpiler uses PLY for lexing and parsing, performs semantic analysis with scoped symbol tables, and generates executable Python.

**Status:** Student project, early stage. Working core pipeline with an eye toward becoming a Python superset. See [docs/FUTURE.md](docs/FUTURE.md) for the vision.

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
├── pyproject.toml          Project metadata, ruff config
├── Dockerfile              Containerised deployment
├── compose.yaml            Docker Compose configuration
└── requirements.txt        Python dependencies
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
