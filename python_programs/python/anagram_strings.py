
def anagram(s1,s2):
    if len(s1) != len(s2):
        return "not a anagram"

    elif sorted(s1) == sorted(s2):
        return "anagram"

    else:
        return "not a anagram"
print(anagram('heart','earth'))
print(anagram('123','231'))