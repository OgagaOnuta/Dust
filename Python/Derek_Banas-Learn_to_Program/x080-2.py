#!/usr/bin/python3

'''
Create a Fibonacci funtion displaying each number in the sequence

1
1
2
3
5
8
13
All Done
'''


def fibonacci(num):
    if (num == 0):
        return (0)
    elif (num == 1):
        return (1)
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return (result)


# Ask how many numbers they want
num = int(input("How many Fibonacci values should be found? "))

# Loop while calling for each new number
i = 1
while (i <= num):
    fibValue = fibonacci(i)

    # Print result and increment
    print(fibValue)
    i += 1

print("All Done")
