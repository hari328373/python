l=list(map(int,input("enter").split()))
s=set(l)
l1=list(s)
print(l1)


s=input('enter:')
l=[]
for i in s:
    if i not in l:
        l.append(i)
    output=''.join(l)
print(output)
