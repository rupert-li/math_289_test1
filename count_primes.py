#!/usr/bin/env python3
"""Count the prime numbers strictly less than n using a sieve."""

import argparse
from math import isqrt


def count_primes(n: int) -> int:
    """Return the number of primes less than n using the Sieve of Eratosthenes."""
    if n <= 2:
        return 0

    is_prime = bytearray(b"\x01") * n
    is_prime[0:2] = b"\x00\x00"

    for candidate in range(2, isqrt(n) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            count = (n - 1 - start) // candidate + 1
            is_prime[start:n:candidate] = b"\x00" * count

    return sum(is_prime)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count primes strictly less than the given integer."
    )
    parser.add_argument("n", type=int, help="upper bound (exclusive)")
    args = parser.parse_args()
    print(count_primes(args.n))


if __name__ == "__main__":
    main()
