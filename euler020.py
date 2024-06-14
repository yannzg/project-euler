# Factorial Digit Sum

import math

x = math.factorial(100)
S = 0
L = [S + int(k) for k in str(x)]
print(sum(L))

