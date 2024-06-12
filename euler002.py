# Even Fibonacci Numbers

def fibonacci_below(n):
    x, y = 0, 1
    L = [x]
    while x <= n:
        if x % 2 == 0:
            L.append(x)
        x, y = y, x + y
    return L


if __name__ == "__main__":
    even_numbers = sum(fibonacci_below(4000000))
    print(even_numbers)

