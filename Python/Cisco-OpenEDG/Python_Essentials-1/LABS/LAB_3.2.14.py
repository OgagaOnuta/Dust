'''
Essentials of the "while" loop
'''

blocks = int(input("Enter the number of blocks: "))

# The number of blocks used is "1 + 2 + ... + n"
# which is equivalent to "(n * (n + 1)) / 2)"
# where n is the height
# => (n**2) + n = 2b, with b representing the number of blocks
# => (n**2) + n - 2b = 0
# => The root of the quadratic equation are
# => "0.5 * (-1 + ((1 + 8b) ** 0.5))" and "0.5 * (-1 - ((1 + 8b) ** 0.5))"

# Taking just postive roots
height = int(0.5 * (-1 + ((1 + (8 * blocks)) ** 0.5)))

print("The height of the pyramid:", height)
