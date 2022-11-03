def printorder(arr,n):
    arr.sort()

    i=0
    j=n-1
    while i<round(n/2):
        print(arr[i])
        i=i+1
    while j>=round(n/2):
        print(arr[j])
        j=j-1

arr=[5,4,6,2,1,3,8,9,7,10]
n=len(arr)
printorder(arr,n)
