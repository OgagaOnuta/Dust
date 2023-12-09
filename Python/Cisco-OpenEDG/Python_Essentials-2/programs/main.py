from sys import path

path.append("..\\modules")

# path.append("C:\\Users\\OgagaOnuta\\Documents\\.Folders\\Tech\\Dust\\Python\\Cisco-OpenEDG\\Python_Essentials-2\\modules")

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.sum1(zeroes))
print(module.prod1(ones))
