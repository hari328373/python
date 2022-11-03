

# equilateral triangle
n=int(input("enter")) #5
for i in range(0,n):#0,1,2,3,4
    for j in range(0,n-i-1):#0,1,2,3
        print(end=" ")
    for j in range(0,2*i+1):#
            print("*",end="")
    print()



n=int(input("enter"))
for i in range(1,n+1):
      print(' '*(n-i),end='')
      for j in range(1,i+1):
          print("*",end=" ")
      print()
