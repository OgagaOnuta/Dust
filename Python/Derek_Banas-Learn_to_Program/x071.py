#!/usr/bin/python3

'''
Create a Fibonacci funtion

1, 1, 2, 3, 5, 8, 13

Fn = Fn-1 + Fn-2
Where F0 = 0 and F1 = 1
'''


def fibonacci(num):
    if (num == 0):
        return (0)
    elif (num == 1):
        return (1)
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return (result)


num = int(input("Enter Fibonacci number: "))
print(fibonacci(num))
