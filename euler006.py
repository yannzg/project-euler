# Sum Square Difference

S1 = 0
S2 = 0
for k in range(1,101):
    S1 += k**2
    S2 += k

S2 = S2**2

if __name__ == "__main__":
    print(S1, S2)
    print(S2 - S1)

