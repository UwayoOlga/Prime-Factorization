from collections import Counter
from prime_factorizer import prime_factors_optimized

def get_factor_counts(n: int) -> Counter:
    return Counter(prime_factors_optimized(n))

def gcd_using_pf(a: int, b: int) -> int:
    fa = get_factor_counts(a)
    fb = get_factor_counts(b)

    gcd = 1
    for p in fa:
        if p in fb:
            gcd *= p ** min(fa[p], fb[p])
    return gcd

def count_divisors(n: int) -> int:
    factors = get_factor_counts(n)
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count

def lcm_using_pf(a: int, b: int) -> int:
    fa = get_factor_counts(a)
    fb = get_factor_counts(b)
    lcm = 1
    all_primes = set(fa) | set(fb)

    for p in all_primes:
        max_exp = max(fa.get(p, 0), fb.get(p, 0))
        lcm *= p ** max_exp
    return lcm

if __name__ == "__main__":
    A = 72
    B = 108 

    print(f"GCD({A}, {B}): {gcd_using_pf(A, B)}")
    print(f"LCM({A}, {B}): {lcm_using_pf(A, B)}")

    print(f"Number of divisors for {A}: {count_divisors(A)}")
    print(f"Number of divisors for {B}: {count_divisors(B)}")