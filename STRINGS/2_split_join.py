# @author: ANISHK YADAV

"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

# CODE:


def split_and_join(line):
    spl = line.split(" ")
    spl = "-".join(spl)
    return spl


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
