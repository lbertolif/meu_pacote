"""Núcleo da biblioteca."""

from __future__ import annotations


def say_hello(name: str = "world") -> str:
    """Retorna uma saudação.

    Args:
        name: nome a ser cumprimentado.

    Returns:
        A saudação formatada.
    """
    return f"hello {name}"
