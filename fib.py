import argparse
from linecache import cache


def fibbonacci_iterative(n: int) -> int:
    """
    Camputes the n-th Fibonacci number.
    :param n: The n-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    for _ in range(n - 1):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return nth


cache = {}


def fibbonacci_recursive(n: int) -> int:
    """
    Camputes the n-th Fibonacci number using cache's memory.
    :param n: The n-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    if n in cache:
        return cache[n]

    nth = fibbonacci_recursive(n - 1) + fibbonacci_recursive(n - 2)
    cache[n] = nth
    return nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='fib',
        description='Fibonacci number generator')

    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")
    args = parser.parse_args()

    result = fibbonacci_recursive(args.nth)
    print(result)
