def gcd(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y

    for i in range(1,smaller+1):
        if((x%i==0) and(y%i==0)):
            gcd=smaller

        return gcd
print(gcd(54,24))