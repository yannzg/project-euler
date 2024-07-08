# Totient Maximum

def euler_totient(n):
    result = n
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            while n % k == 0:
                n //= k
            result *= (1 - 1/k)
    if n > 1:
        result *= (1 - 1/n)
    return int(result)

max_ntotient = 0
max_n = 0

for i in range(2, 1000001):
    totient = euler_totient(i)
    ntotient = i / totient
    if ntotient >= max_ntotient:
        max_ntotient = ntotient
        max_n = i

if __name__ == "__main__":
    print(max_n)