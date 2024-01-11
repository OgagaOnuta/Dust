#!/usr/bin/python3

import time

def merry_christmas(n: int = 30):
    for i in range(1, n, 2):
        print(("*" * i).center(n))
        time.sleep(0.2)
    for j in range(int(n / 9)):
        print(("|||").center(n))
        time.sleep(0.2)
    print(("[][][][][][]").center(n))

merry_christmas(30)
