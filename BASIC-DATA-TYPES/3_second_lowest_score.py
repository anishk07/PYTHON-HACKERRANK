# @author: ANISHK YADAV

"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

# CODE:

record = []
marks = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        info = [name, score]
        record.append(info)
        marks.append(score)

# sort the record alphabetically
record.sort()
# print(record)

# sort the marks and find the second lowest score
marks.sort(reverse=True)
second_lowest_score = marks[(marks.index(min(marks)))-1]

# run a loop through record and print the student's name with second lowest score
for i, j in record:
    if j == second_lowest_score:
        print(i)
