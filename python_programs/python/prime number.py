
def isprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "not a prime"
                break
        else:
            return "prime"

    else:
        print('not a prime')
print(isprime(21))
