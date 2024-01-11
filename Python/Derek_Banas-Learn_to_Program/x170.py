#!/usr/bin/python3

import re

randStr = "https://www.youtube.com http://www.google.com"

# REQUIRED OUTPUT
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>

# MY SOLUTION
# regex = re.compile(r"([\w]{4,5}://)([\w]{3}.[\w]{6,7}.[\w]{3})")
# randStr = re.sub(regex, r"<a href='\1\2'>\2</a>\n", randStr)

# DEREK BANAS SOLUTION
regex = re.compile(r"(https?://([\w.]+))")
randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

print(randStr)
