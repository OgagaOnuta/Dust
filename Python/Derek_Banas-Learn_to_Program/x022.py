#!/usr/bin/python3

# Ask for the tree height
tree_height = int(input("Height of tree: "))
leaf_width = 1
space_width = tree_height - 1
stump_space = tree_height - 1

# Loop height times
i = 0
while (i < tree_height):
    # Print space and leaf
    print(" " * space_width, "*" * leaf_width)
    leaf_width += 2  # Increase leaf_width by 2
    space_width -= 1  # Decrease space_width by 1
    i += 1

# Print stump of tree
print(" " * stump_space, "#")
