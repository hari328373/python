# string palindrome and number
def palindrome(n):
    if n==n[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
print(palindrome('123'))


# number palindrome
def palindrome(n):
    temp=n
    rev=0
    while n!=0:
        r=n % 10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        print( 'palindrome')
    else:
        print('not a palindrome')
print(palindrome(121))