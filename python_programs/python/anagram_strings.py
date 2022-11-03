'''n1=input('enter1:')
n2=input('enter2:')

n1=sorted(n1)
n2=sorted(n2)

if len(n1)!=len(n2):
    print("not a anagram")

elif n1==n2:
    print("anagram")

else:
    print("not a anagram")'''

def anagram(s1,s2):
    if len(s1) != len(s2):
        return "not a anagram"

    elif sorted(s1) == sorted(s2):
        return "anagram"

    else:
        return "not a anagram"
print(anagram('heart','earth'))
print(anagram('123','231'))