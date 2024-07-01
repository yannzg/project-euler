# Square Digit Chains

L = []    

def square_digit_chain(number):
    seen = set()
    while number != 89:
        if number in seen:
            return False
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number)) 
    return True

for i in range(1, 10000001):
    if square_digit_chain(i) == True:
        L.append(i)

total = len(L)
print(total) # A bit slow but gets the job done