def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True

    return leap
print(is_leap(1998))
print(is_leap(2000))