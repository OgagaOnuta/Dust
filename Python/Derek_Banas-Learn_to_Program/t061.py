#!/usr/bin/python3

'''
BUBBLE SORT
===========

1. An outer loop decreases in size each time
2. The goal is to have largest number at the end of the list
   when the outher loop completes one cycle
3. The inner loop starts comparing indexes at the beginning
   of the loop
4. Check if list[index] > list[index + 1]
5. If so, swap the index values
6. When the inner loop completes, the largest number is at the
   end of the list
7. Decrement the outer loop by 1
'''

import random

randList = []

for i in range(5):
    randList.append(random.randrange(1, 10))

print(randList)

i = len(randList) - 1
while (i > 1):
    j = 0
    while (j < i):
        print("\nIs {} > {}".format(randList[j], randList[j + 1]))

        if (randList[j] > randList[j + 1]):
            print("Switch")

            temp = randList[j]
            randList[j] = randList[j + 1]
            randList[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        m = len(randList) - 1
        for k in randList:
            print(k, end="")
            if (m != 0):
                print(", ", end="")
            m -= 1
        print()

    print("END OF ROUND")
    i -= 1

print()
# for k in randList:
#     print(k, end=", ")

print(randList)
