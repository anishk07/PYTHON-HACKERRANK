# @author: ANISHK YADAV

"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

# CODE:


def swap_case(s):
    newst = ''
    for a in s:
        if (a.islower()) == True:
            newst += (a.upper())
        elif (a.isupper()) == True:
            newst += (a.lower())
        else:
            newst += a
    return newst


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
