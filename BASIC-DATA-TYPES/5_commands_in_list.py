# @author: ANISHK YADAV

"""
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""


list_of_integers = []

# take the number of commands from user
N = int(input())

# loop over the given number of commands
for i in range(N):
    cmd = input().split()  # split and store the command in the list
    if cmd[0] == 'insert':
        list_of_integers.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(list_of_integers)
    elif cmd[0] == 'remove':
        list_of_integers.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        list_of_integers.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list_of_integers.sort()
    elif cmd[0] == 'pop':
        list_of_integers.pop()
    elif cmd[0] == 'reverse':
        list_of_integers.reverse()
    else:
        print("INVALID COMMAND!")
