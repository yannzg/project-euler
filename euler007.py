# 10001st Prime

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            return False
    return True

def find_prime():
    count = 0
    n = 2
    primes = []

    while len(primes) < 10001:
        if is_prime(n) == True:
            primes.append(n)
        n += 1
    
    return primes[-1]

if __name__ == "__main__":
    print(find_prime())


    
