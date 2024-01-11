#!/usr/bin/python3

'''
List Comprehension return lists
'''

multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])
print([vert[2] for vert in multiList])
print([multiList[i][i] for i in range(len(multiList))])
