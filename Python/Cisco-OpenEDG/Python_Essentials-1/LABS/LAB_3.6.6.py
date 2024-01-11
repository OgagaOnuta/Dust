'''
Operating with lists - basics
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Create new list containing just the first element of the list to be checked
new_list = [my_list[0]]

# Loop through list to be checked
for i in my_list:
	# If element is not in new list, append to new list
	if (i not in new_list):
		new_list.append(i)

# Point previous list to new list
my_list = new_list

print("The list with unique elements only:")
print(my_list)
