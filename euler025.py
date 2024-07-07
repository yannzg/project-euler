# 1000-digit Fibonacci Number

def fibonacci():
    x = 1
    y = 1
    n = 2
    while len(str(y)) < 1000:
        x, y = y, x + y
        n += 1
    return n

if __name__ == "__main__":
    print(fibonacci())