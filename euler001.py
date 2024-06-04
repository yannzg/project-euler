# Multiples of 3 or 5

n = 1000

L = []
for k in range(1, n):
    if k % 3 == 0:
        L.append(k)
    elif k % 5 == 0:
        L.append(k)
    
print(L)

list = list(set(L))
print(list)

S = 0
for x in list:
    S += x

print(S)
