# Multiples of 3 or 5

print(sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1000))))
