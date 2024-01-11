#!/usr/bin/python3

'''
THREADS are like running multiple programs at once.

Threads take turns executing, while one is executing,
the other sleeps until it's its turn to execute.

A Thread is a block of code that executes.
'''

import random
import threading
import time


def executeThread(i):
    print("Thread {} sleeps at {}".format(
        i, time.strftime("%H:%M:%S", time.gmtime())
    ))

    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at {}".format(
        i, time.strftime("%H:%M:%S", time.gmtime())
    ))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads:", threading.active_count())
    print("Thread Objects:", threading.enumerate())
