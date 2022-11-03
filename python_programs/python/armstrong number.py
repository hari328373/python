def armstrong_num(n):
    l=len(str(n))
    sum=0
    temp=n

    while n>0:
        r=n%10
        sum=sum+r**l
        n=n//10
    if sum==temp:
        return temp,"armstrong number"
    else:
        return temp,"not a armstring number"
print(armstrong_num(374))
print(armstrong_num(371))