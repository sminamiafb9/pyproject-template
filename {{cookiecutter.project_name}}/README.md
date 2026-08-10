# {{cookiecutter.project_name}}

## Development

### Requirements

- Python
- uv

Python環境および依存管理には `uv` を利用する。

---

### Setup

#### Install dependencies

```bash
uv sync
```

---

#### Run

```bash
uv run <command>
```

### Development Tools

本プロジェクトでは、開発環境とコード品質を維持するために以下のツールを利用します。

| Tool | Purpose |
| --- | --- |
| uv | Python環境・依存管理 |
| Ruff | Lint / Format |
| Pyright | Static Type Check |
| pytest | Test Framework |
| poethepoet | Development Task Runner |

---

#### Lint/Format

```bash
uv run poe lint
uv run poe format
```

---

#### Type Check


```bash
uv run poe typecheck
```

---

#### Test

```bash
uv run poe test
```

---

#### Task Runner

[poethepoet] を利用して開発コマンドを管理します。

開発時に必要なコマンドを `pyproject.toml` に定義し、実行手順をコード化します。

```bash
# Lint / Format / Type Check / Test を実行
uv run poe check
```
