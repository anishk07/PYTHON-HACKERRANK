# @author: ANISHK YADAV

"""
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
"""

# CODE:

import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    s_string = wrapper.fill(text=string)

    return s_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
