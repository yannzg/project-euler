# Summation of Primes

from math import isqrt

def sieves(n):
    
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False

    for k in range(2, isqrt(n) + 1):
        if prime[k] == True:
            for i in range(k**2, n +1, k):
                prime[i] = False

    return [k for k in range(n+1) if prime[k] == True]

print(sum(sieves(2000000)))