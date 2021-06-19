# @author: ANISHK YADAV

"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

# CODE:

N, M = [int(x) for x in input().split()]
design = ['.|.' * (2 * i + 1) for i in range(N//2)]
string = 'WELCOME'
r_design = design[::-1]

for i in design:
    print(i.center(M, '-'))
print(string.center(M, '-'))
for i in r_design:
    print(i.center(M, '-'))
