# Python Project Template

Pythonプロジェクトの開発に必要なツール・設定をあらかじめ整備したCookiecutterテンプレートです。

プロジェクトごとに繰り返し行っている初期設定をテンプレート化し、同じ開発環境を再利用できるようにすることを目的としています。

## 特徴

### 開発環境

| 用途 | ツール |
|---|---|
| Python / Package Management | uv |
| Containerized Development | Dev Container |
| Editor | VS Code Profile |

### 開発ツール

| 用途 | ツール |
|---|---|
| Lint / Format | Ruff |
| Type Check | Pyright |
| Test | pytest |
| Test Coverage | pytest-cov |
| Randomized Test Execution | pytest-randomly |
| Task Runner | poethepoet |
| Git Hook | pre-commit |

### 自動化

プロジェクト生成後に以下を自動的にセットアップします。

- Git Repositoryの初期化
- Python依存関係のインストール
- pre-commit hookの登録

また、Git commit時には `poe check` を実行し、Lint / Format / Type Check / Test / Buildをまとめて実行します。

## 使い方

### 前提

以下をローカル環境にインストールしてください。

- Git
- Python
- uv
- Cookiecutter

Cookiecutterはuvを利用してインストールできます。

```bash
uv tool install cookiecutter
```

### プロジェクトの生成

```bash
cookiecutter gh:sminamiafb9/pyproject-template
```

プロジェクト名などを入力すると、プロジェクトが生成されます。

## 生成後の初期化

プロジェクト生成時に以下の初期化処理が実行されます。

```text
git init
uv sync
uv run pre-commit install
```

そのため、生成後はそのまま開発を開始できます。

## 開発コマンド

開発用コマンドはpoethepoetで管理しています。

### Check

Lint / Format / Type Check / Test / Buildをまとめて実行します。

```bash
uv run poe check
```

### Format

```bash
uv run poe format
```

### Lint

```bash
uv run poe lint
```

### Type Check

```bash
uv run poe typecheck
```

### Test

```bash
uv run poe test
```

`pytest-cov` によりパッケージのカバレッジを計測します。結果はターミナルに表示され、HTMLレポートは `htmlcov/index.html` に出力されます。

`pytest-randomly` によりテストはランダムな順序で実行されます。順序に依存しないテストを維持してください。

### Build

```bash
uv run poe build
```

ビルド成果物は `dist/` に出力されます。

## pre-commit

Git commit時に `poe check` が自動的に実行されます。

```text
git commit
    ↓
pre-commit
    ↓
uv run poe check
    ├── format
    ├── lint
    ├── typecheck
    ├── test
    └── build
```

手動で実行する場合は、

```bash
uv run pre-commit run --all-files
```

を使用します。

## Dev Container

開発環境としてDev Containerを利用できます。

Dev Containerでは以下を提供します。

- Python 3.12
- uv

uvはDev ContainerのDockerfileから公式インストーラーを利用してインストールします。

コンテナ作成後に、

```bash
uv sync
uv run pre-commit install
```

を実行します。

VS Codeの拡張機能については、プロジェクトではなくVS Code Profileで管理します。

RuffについてはDev Containerの設定からRuff拡張をインストールします。

## プロジェクト構成

生成されるプロジェクトは以下の構成を基本とします。

```text
<project_name>/
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── pyrightconfig.json
├── README.md
├── src/
│   └── <package_name>/
│       └── __init__.py
└── tests/
    └── test_sample.py
```

## 設計方針

各ツールの責務を分離し、プロジェクト設定をシンプルに保ちます。

| ツール | 役割 |
| --- | --- |
| Cookiecutter | プロジェクトのテンプレート生成 |
| uv | Python環境・依存関係管理 |
| Ruff | Lint / Format |
| Pyright | Type Check |
| pytest | Test |
| pytest-cov | Test Coverage |
| pytest-randomly | Randomized Test Execution |
| poethepoet | 開発コマンド管理 |
| pre-commit | commit前のチェック |
| Dev Container | 開発環境の提供 |
| VS Code Profile | VS Code拡張の管理 |

## カスタマイズ

テンプレートの設定は、生成されるプロジェクトの `pyproject.toml` や `devcontainer.json` などを変更することでカスタマイズできます。

Cookiecutterの入力項目を変更する場合は、`cookiecutter.json` を編集してください。

## 更新方法

テンプレートを更新した場合、既に生成済みのプロジェクトには自動的には反映されません。

既存プロジェクトへの変更は、必要に応じて個別に適用してください。

## 注意事項

このテンプレートは汎用的なPython開発環境を提供することを目的としています。

プロジェクト固有のライブラリや設定については、生成後のプロジェクト側で追加してください。
