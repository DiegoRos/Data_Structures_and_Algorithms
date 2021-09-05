def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError
    
    return n * factorial(n-1)


def fibonacci(n):
    if n < 0:
        raise ValueError

    elif n == 0:
        return 0
    
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def reverse_string(str):
    if len(str) == 0:
        return ""
    
    return reverse_string(str[1:]) + str[0]


if __name__ == "__main__":
    n = 0
    print(f"{n}! =", factorial(n))

    n2 = 19
    print(f"Fibonacci of 5 is:", fibonacci(n2))

    str = "Hello my name is Diego"
    print(reverse_string(str))
