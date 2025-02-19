# Largest Prime Factor

# Using trial division

def largest_prime(n):
    while n % 2 == 0: 
        largest_prime = 2
        n = n // 2 
    for k in range(3, int(n**(1/2)) +1, 2): 
        while n % k == 0: 
            largest_prime = k
            n = n // k 
    if n > 2: 
        largest_prime = n
    return largest_prime

if __name__ == "__main__":
    print(largest_prime(600851475143))
