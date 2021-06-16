# @author: ANISHK YADAV

"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""

# CODE:


def count_substring(string, sub_string):
    cnt = 0
    sub_l = len(sub_string)
    for i in range(0, len(string)):
        st = str(string[i:i+sub_l])
        if st == sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
