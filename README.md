# meu-pacote

Biblioteca de exemplo distribuível, Python 3.14, gerenciada com **uv**.

## Instalação

```bash
uv venv
uv sync
```

## Uso

```python
from meu_pacote import say_hello

print(say_hello("Lucas"))  # hello Lucas
```

## Desenvolvimento

```bash
uv run ruff check .
uv run mypy src
uv run pytest --cov
```

## Publicação

```bash
uv build
twine upload dist/*
```
