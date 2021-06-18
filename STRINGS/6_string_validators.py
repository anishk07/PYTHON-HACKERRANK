# @author: ANISHK YADAV

"""
Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""

# CODE:

if __name__ == '__main__':
    s = input()

    # Check For Any Element In The String With any() Function.
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
