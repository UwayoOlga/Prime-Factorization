import math 
from collections import Counter

def prime_factors_optimized(n: int) -> list[int]:
    if n <= 1:
        return []
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    test_number = 84
    print(f"Prime factors of {test_number}: {prime_factors_optimized(test_number)}")


