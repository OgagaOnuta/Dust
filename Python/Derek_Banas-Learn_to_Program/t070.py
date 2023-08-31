#!/usr/bin/python3

'''
Dictionaries are similar to Lists,
but use a "key: value" pair
They are non-sequential
'''

davidDict = {"fName": "David", "lName": "Onuta", "address": "Akoka"}

print("My name:", davidDict["fName"])
print()

davidDict["address"] = "Island"
print(davidDict)  # It may not print out in the exact order

davidDict["city"] = "Lagos"
print(davidDict)

print("Is there a city?", "city" in davidDict)
print()

print(davidDict.values())
print(davidDict.keys())
print()

# Looping through the key and values
for k, v in davidDict.items():
    print(k, ":", v)
print()

print(davidDict.get("mName", "Not Here"))
print(davidDict.get("lName", "Not Here"))
print()

del davidDict["fName"]
# Looping through the dictionary keys
for i in davidDict:
    print(i)
print()

davidDict.clear()  # Clearing/Deleting all data in the dictionary
print(davidDict)
print()

employees = []
fName, lName = input("Enter Employee Name: ").split()

employees.append({"fName": fName, "lName": lName})
print(employees)
