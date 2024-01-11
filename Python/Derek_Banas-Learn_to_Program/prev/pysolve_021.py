#!/usr/bin/python3

# My Solution
# Receive height of tree from user
height = eval(input("How tall is the tree: "))

i = height - 1  # Get the length of the space in the first row of the tree
j = i  # Store the length to use for the stump of the tree
length = 1  # Get the length of the tree in the first row

# Use a loop to cycle through and print tree of given length
while (height):
    print(" " * i + "#" * length)
    i -= 1  # Decrement space length by 1
    length += 2  # Increment tree length by 2
    height -= 1  # Decrement tree height by 1

# Print the Stump of the tree
print(" " * j + "#")


'''
# Derek Banas Solution
tree_height = input("How tall is the tree : ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")

    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end="")
print('#')
'''
