# Largest Exponential

# a**b > c**d <=> b·log(a) > c·log(d)

import math
    
L = []

with open("resources/0099_base_exp.txt", 'r') as file:
    text = file.readlines()
    for number in text:
        base, exp = map(int, number.strip().split(','))
        value = exp * math.log10(base)
        L.append(value)

index = 0
max_index = 0
max_value = L[0]

while index < len(L):
    if max_value < L[index]:
        max_index = index 
        max_value = L[index]
    index += 1     


print(max_index + 1)