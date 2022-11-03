def factorial(n):
    f = 1
    if n < 0:
        print("invalid")
    elif n == 0:
        print("factorial=1")
    else:
        for i in range(1, n + 1):
            f = f * i
        return f


print(factorial(5))


# recursion
def factorial(n):
    if n < 0:
        print("invalid")
    elif n == 0:
        return 1
    else:
        res = n * factorial(n - 1)
        return res


print(factorial(6))
