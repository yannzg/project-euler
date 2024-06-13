# Special Pythagorean Triplet

from math import prod

a, b, c = 1, 2, 3
triplets = []

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b 
        if a**2 + b**2 == c**2 and c > b:
            print(f"Triplet: ({a}, {b}, {c})")
            triplets.append((a, b, c))
            break
if triplets:
    triplet = triplets[0]
    product = prod(triplet)
print(product)