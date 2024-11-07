import pytest

from fib import fibbonacci_iterative, fibbonacci_recursive


def test_fib_9_is_34():
    assert fibbonacci_iterative(9) == 34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibbonacci_iterative(-1)


def test_fib_9_is_34_recursive():
    assert fibbonacci_recursive(9) == 34
