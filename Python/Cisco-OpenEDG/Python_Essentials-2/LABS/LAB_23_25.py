'''
You own split
'''


def mysplit(strng):
    # Create empty list
    str_list = []
    
    # If parameter is an empty string, return empty list
    if (strng == ""):
        return (str_list)
    
	# Create empty word string
    word = ""

	# Iterate through the string parameter
    for i in strng:
        # Check for whitespace
        if (i == " "):
            # If word is not empty, append to list, and reset word
            if (len(word) > 0):
                str_list.append(word)
                word = ""
            # If whitespace, skip iteration
            continue
        # If not whitespace, append character to word
        else:
            word += i

    # Append last word to list if word is not empty
    if (len(word) > 0):
        str_list.append(word)
            
	# Return list
    return (str_list)


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
