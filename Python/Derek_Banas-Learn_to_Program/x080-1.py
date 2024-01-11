#!/usr/bin/python3

'''
Display a Fibonacci sequence

1
1
2
3
5
8
13
All Done
'''

# Create initial sequence of 0 and 1
# fibSeq = [0, 1]
fibSeq = [1, 1]


# Create fibonacci function with length of the sequence as argument
def fibonacci(length):
    # Create a loop to run for the required length minus 2
    for i in range(length - 2):
        # Sum the last two values in the sequence and append to sequence
        newItem = fibSeq[i] + fibSeq[i + 1]
        fibSeq.append(newItem)

    for i in fibSeq:
        print(i)

    print("All Done")


seqLen = int(input("Length of Fibnacci sequence: "))
fibonacci(seqLen)
