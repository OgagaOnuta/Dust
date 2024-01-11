'''
Interactive Bubble Sort
'''

my_list = []
swapped = True
num = int(input("How manu elements do you want to sort: "))

for i in range(num):
	val = float(input("Enter a list element: "))
	my_list.append(val)

while (swapped):
	swapped = False

	for i in range(len(my_list) - 1):
		if (my_list[i] > my_list[i + 1]):
			swapped = True
			my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:\t")
print(my_list)
