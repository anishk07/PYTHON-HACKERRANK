# @author: ANISHK YADAV

"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
"""

# CODE:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # store the array items in the list and then sort it
    l = list(arr)
    l.sort()

    # print(max(l))

    # print the value of element index 1 less than the index value of max of list
    print(l[(l.index(max(l)))-1])
