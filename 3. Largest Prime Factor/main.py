def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

allPrimeFactors = prime_factors(600851475143)
maxPrimeFactor = max(allPrimeFactors)
print("LPF:", maxPrimeFactor)