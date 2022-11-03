def fib(n):
    a,b=0,1
    if n<0:
        print("incorrect")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
print(fib(5))

#recursion
def fib(n):
    if n<0:
        print("invalid")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

