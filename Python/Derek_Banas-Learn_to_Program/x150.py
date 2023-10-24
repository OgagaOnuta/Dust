#!/usr/bin/python3

'''
Match email addresses

1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
2. An @ symbol
3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
4. A period
5. 2 to 3 lowercase and uppercase letters
'''

import re

emailList = "db@aal.com m@.com @apple.com db@.com eat@email.com"
email = re.findall(r"[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}", emailList)

print("Email Matches:", len(email))
