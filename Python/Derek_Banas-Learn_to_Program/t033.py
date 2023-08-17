#!/usr/bin/python3

'''
The type() function returns the type of the object passed to it
The len() function returns the length of a string
The str() function converts the input to a string
The ord() function converts characters to ASCII unicode
The chr() function converts ASCII unicode to characters
'''

samp_string = "This is a very important string"
print(samp_string[0])
print(samp_string[3 + 5])
print(samp_string[-1])

print()
print("Length: ", len(samp_string))  # Length of a string
print(samp_string[0:4])  # 0 to 3rd index, excluding the 4th index
print(samp_string[8:])  # From the 8th index to the end
print("Green " + "Eggs")
print("Hello " * 5)

num_string = str(4)  # Convert integer to string

print()
for char in samp_string:
    print(char)

print()
for i in range(0, (len(samp_string) - 1),  2):
    print(samp_string[i] + samp_string[i + 1])

print()
# Converting characters to unicode and vice-versa
print("A = ", ord("A"))
print("65 = ", chr(65))
