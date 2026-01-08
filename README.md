# Prime Factorization Algorithm
 
**Prime factorization** is the process of breaking a number down into a **product of prime numbers**.

> A **prime number** is a number greater than 1 that has exactly two factors: 1 and itself
> Examples: 2, 3, 5, 7, 11 …

##  Idea Behind the Algorithm

Every whole number **greater than 1** can be written **uniquely** as a product of prime numbers.

Example:

```
60 = 2 × 2 × 3 × 5 = 2² × 3 × 5
```

##  Prime Factorization Algorithm (Step-by-Step)

### Input: a number `n > 1`

### Output: its prime factors

###   Step 1: Start with the smallest prime

Begin dividing by **2** (the smallest prime).

###  Step 2: Divide as long as possible

* If `n` is divisible by the current divisor:

  * Record the divisor
  * Replace `n` with `n ÷ divisor`
* If not divisible:

  * Move to the **next prime number** (3, 5, 7, …)

### Step 3: Stop condition

Stop when `n = 1`
OR when the divisor² > n (then `n` itself is prime)

## Example Walkthrough

### Factorize **180**

| Step | n   | Divisor | Action       |
| ---- | --- | ------- | ------------ |
| 1    | 180 | 2       | 180 ÷ 2 = 90 |
| 2    | 90  | 2       | 90 ÷ 2 = 45  |
| 3    | 45  | 3       | 45 ÷ 3 = 15  |
| 4    | 15  | 3       | 15 ÷ 3 = 5   |
| 5    | 5   | 5       | 5 ÷ 5 = 1    |

### Result:

```
180 = 2² × 3² × 5
```

## Pseudocode (Algorithm Form)

```text
function primeFactorization(n):
    for i from 2 to √n:
        while n mod i == 0:
            print i
            n = n / i
    if n > 1:
        print n
```

## Time Complexity

* Worst case: **O(√n)**
* Efficient for small to medium numbers

## Why It’s Important

Prime factorization is used in:

* Finding **GCD & LCM**
* Cryptography (RSA)
* Simplifying fractions
* Number theory problems

##  Another Quick Example

```
84 = 2 × 2 × 3 × 7 = 2² × 3 × 7
```
 
