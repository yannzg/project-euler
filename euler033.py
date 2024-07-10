# Digit Cancelling Fractions

from fractions import Fraction

L = []

# Generating all the fractions

for i in range(10, 100):
    for j in range(10, i):
        frac = f"{j}/{i}"
        L.append(frac)


# Each fraction is assigned its simplified version if it exists

simplified_fractions = {}

for x in L:
    n = Fraction(x).numerator
    d = Fraction(x).denominator
    simplified_fractions[f"{x}"] = f"{n}/{d}"


# Removing fractions that can't be simplified

removed_fractions = [key for key, value in simplified_fractions.items() if key == value]
for key in removed_fractions:
    del simplified_fractions[key]

# Removing fractions which:
# - numerator and denominator do not have a common digit 
# - contain a multiple of 11 
# - are trivial, i.e. contain two multiple of 10 (e.g. 40/50)

to_be_removed_fractions = []

for key, value in simplified_fractions.items():
    digits = [key[i] for i in [0, 1, 3, 4]]
    if len(set(digits)) == 4: 
        to_be_removed_fractions.append(key)
    if key[0] == key[1] or key[3] == key[4]:
        to_be_removed_fractions.append(key)
    if int(key[0:2]) % 10 == 0 and int(key[3:5]) % 10 == 0:
        to_be_removed_fractions.append(key)

for key in to_be_removed_fractions:
    del simplified_fractions[key]


S = []
for key, value in simplified_fractions.items():
    for i in [0, 1]:
        for j in [3, 4]:
            if f"{key[i]}/{key[j]}" == f"{value}":
                S.append(key)

for key in S:
    print(f"{key} = {simplified_fractions[key]}")


