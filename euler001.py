# Multiples of 3 or 5

n = 1000

print(sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1000))))
