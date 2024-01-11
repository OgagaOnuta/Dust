'''
Uniteractive Bubble Sort
'''

my_list = [8, 10, 6, 2, 4]  # List to sort

print("List to sort:\t", my_list)

swapped = True  # It's a little fake , we need it to enter the while loop.

while (swapped):
	swapped = False  # No swaps so far

	for i in range(len(my_list) - 1):
		if (my_list[i] > my_list[i + 1]):
			swapped = True  # A swap occurred!
			my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Bubble Sort:\t", my_list)
