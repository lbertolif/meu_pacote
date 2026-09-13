"""Testes do núcleo."""

from meu_pacote import say_hello


def test_default() -> None:
    assert say_hello() == "hello world"


def test_custom_name() -> None:
    assert say_hello("Lucas") == "hello Lucas"
