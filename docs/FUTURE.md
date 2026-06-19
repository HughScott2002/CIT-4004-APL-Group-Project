# TypeSnake Future

## Vision

TypeSnake as a development platform — not just a language.

```
tsnake init my-app     # scaffold
tsnake run             # run like python
tsnake check           # type-check only
tsnake build -o build/ # transpile .ts -> .py
```

Under the hood it wraps `uv` (env/pkg management) and `ruff` (fmt/lint). Swappable interpreter via `--interpreter cpython|rustpython|pypy`. The transpiler output is valid Python — any third-party package works.

## Architecture: transpiler with optional macros

Own parser, own AST, custom syntax. Codegen emits plain Python. No CPython AST extensions needed.

```
Source (.ts)
  ↓
Tokenizer (extended Python tokens)
  ↓
Macro expander (transform token stream)
  ↓
Parser (Python grammar + macro call sites)
  ↓
Custom AST
  ↓
Type checker (walk custom AST)
  ↓
Desugarer (expand syntax sugar -> Python-compatible AST)
  ↓
Code generator (ast.unparse or string builder)
  ↓
Valid Python (.py)
```

### Macro system decision

Options debated:
1. **Rust-style declarative macros** — pattern-match on token trees, rewrite. Powerful, complex.
2. **Terser-style compile-time functions** — macros are Python functions that receive/return AST nodes. Simpler.
3. **No macro system, hardcode each feature** — most predictable, most work per feature.

**Decision:** Start without macros. Hardcode first features (`?.`, `??`, safe indexing, `Result`/`Option` typed wrapping). If patterns emerge, build macros in v2.

## Parse strategy: AST transform vs forked parser

Three approaches:

| Approach | Pro | Con |
|---|---|---|
| **AST transform** (`ast.parse` + walk + validate + codegen) | Free Python compat, no parser to maintain | Can't add syntax that CPython can't parse |
| **Fork Python grammar** (Lark/PEG) | Full control over syntax | Must track CPython grammar changes |
| **Monkeypatch CPython's parser** | New syntax without full rewrite | Fragile, unmaintainable |

**Decision:** Since we want new syntax (and possibly macros), we own the parser. Must ensure 100% of valid Python also parses as valid TypeSnake.

## Language design: Python superset

- 100% Python-compatible. Every `.py` is valid `.ts`.
- Add mandatory type annotations (opt-in per file or project).
- Add sugar: `.collect()`, `?.`, `??`, safe subscript, `Result[T, E]`, `Option[T]`, pattern matching.
- No compatibility tax: transpiler output is plain Python.

## Open problems

### 1. Untyped import boundary

What happens at `import requests`?

Options:
- Skip type checking on imports (pragmatic, most third-party code is untyped)
- Require `.pyi` stub; `tsnake stub-gen` generates stubs from installed packages
- Pyright integration for `.pyi`-less inference

**Decision:** Unresolved. Simplest correct answer — imports resolve to `Any` by default, `.pyi` stubs opt-in.

### 2. Phasing

Two axes, which first?

- **CLI first:** Wrap uv/ruff, works on normal Python today. Language improvements second.
- **Language first:** Rewrite the compiler to superset. CLI second.

### 3. Name

"TypeSnake" was the old custom-syntax language. Keep it for the Python superset? Or rename?

## Current state (June 2026)

- PLY-based lexer + parser + semantic analyzer + code generator: ~1500 LOC
- Custom syntax: `scribe`/`hail`/`lock`/`unlock`/`attempt`/`findout`/`@` line endings
- Flask API server with `exec()` in prod (critical RCE — must fix)
- Zero tests, zero type hints in the Python codebase
- Azure Web App CI/CD configured
- Working Docker build

### What's salvageable

- `symbol_table.py` scoping logic and `FunctionSymbol`/`VariableSymbol` classes
- Parts of `semantic_analyzer.py` type checking logic
- General pipeline concept

### What gets rewritten

- Lexer (need to handle Python tokens + extensions)
- Parser (need to parse Python, not custom syntax)
- Code generator (need to emit standard Python, not `exec`-based)
- CLI tool (new)

## Production hardening needed (if the server stays)

- Remove `exec()` — transpile only, let the caller run the output
- Remove `debug=True`
- Fix CORS (remove `"*"` wildcard)
- Add tests before anything else
- Add `.gitignore`, `pyproject.toml`, ruff config
- Rotate the exposed Azure secret in CI/CD
- Add rate limiting, input validation, health check endpoint
