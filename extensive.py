from prime_factorizer import prime_factors_optimized
from collections import Counter
import time

def format_factorization(n: int) -> str:
    factors = prime_factors_optimized(n)
    if not factors:
        return "No prime factors (n <= 1)"
    
    counts = Counter(factors) 
    parts = []
    for p in sorted(counts.keys()):
        exp = counts[p]
        if exp > 1:
            parts.append(f"{p}^{exp}")
        else:
            parts.append(f"{p}")
    
    return " * ".join(parts)

def run_demo():
    print("=" * 50)
    print("      PRIME FACTORIZATION ")
    print("=" * 50)
    
    test_cases = [
        12,        # Small composite
        84,        # Medium composite
        100,       # Square
        101,       # Prime
        1024,      # Power of 2
        9999,      # Large composite
        1000003    # Large prime  
    ]
    
    for n in test_cases:
        print(f"Factoring {n}...")
        start = time.time()
        result = format_factorization(n)
        end = time.time()
        print(f"  Result: {n} = {result}")
        print(f"  Time taken: {(end - start) * 1000:.4f}ms")
        print("-" * 30)

    print("\n[Interactive Mode]")
    try:
        while True:
            val = input("Enter a number to factor (or 'q' to quit): ")
            if val.lower() == 'q':
                break
            n = int(val)
            print(f"  {n} = {format_factorization(n)}")
    except ValueError:
        print("Exiting interactive mode.")
    except KeyboardInterrupt:
        print("\nDemo stopped.")

if __name__ == "__main__":
    run_demo()
