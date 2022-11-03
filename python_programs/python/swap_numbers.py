#swaping
x=int(input("enter x: "))
y=int(input("enter y: "))
x,y=y,x
print("after swapping of x",x)
print("after swapping of y",y)

# with third variable
x=int(input("enter x: "))
y=int(input("enter y: "))

temp=x
x=y
y=temp
print("after swapping of x",x)
print("after swapping of y",y)

x=int(input("enter x: "))
y=int(input("enter y: "))
x=x+y
y=x-y
x=x-y
print("after swapping of x",x)
print("after swapping of y",y)
