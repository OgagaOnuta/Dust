#!/usr/bin/python3

'''
1. Create a file named "mydata2.txt"
2. Use what was learned in Part 8 to find out
   how to open a file without `with` (Open in try)
3. Catch FileNotFoundError
4. In `else`, print contents
5. In `finally`, print any message
6. Open non-existent file "mydata3.txt"
'''

myFile2 = open("mydata2.txt", mode="w", encoding="utf-8")

myFile2.write("This is a random file.\n\
This file is created for practice purposes.\n\
Let's learn together.\n")

myFile2.close()

try:
    # myFile3 = open("mydata2.txt", mode="r", encoding="utf-8")
    myFile3 = open("mydata3.txt", mode="r", encoding="utf-8")
except (FileNotFoundError):
    print("FILE NOT FOUND")
else:
    print(myFile3.read())
    myFile3.close()
finally:
    print("If existing file was provided, above are the contents")
