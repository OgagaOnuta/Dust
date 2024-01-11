'''
Find the greater value in a list
'''

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13, 20]
largest = my_list[0]

for i in range(1, len(my_list)):
	if (my_list[i] > largest):
		largest = my_list[i]

'''
# This will compare the first element with itself
for i in my_list:
	if (i > largest):
		largest = i
'''

'''
for i in my_list[1:]:
	if (i > largest):
		largest = i
'''

print(largest)
