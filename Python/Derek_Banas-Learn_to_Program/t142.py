#!/usr/bin/python3

'''
Whenever you're using your thread, you can lock other threads from executing.
'''

import random
import threading
import time


class BankAccount(threading.Thread):
    accountBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(
            customer.name, customer.moneyRequest,
            time.strftime("%H:%M:%S", time.gmtime())
        ))

        if ((BankAccount.accountBalance - customer.moneyRequest) > 0):
            BankAccount.accountBalance -= customer.moneyRequest

            print("New account balance: ${}".
                  format(BankAccount.accountBalance))
        else:
            print("Not enough money in account")
            print("Current balance: ${}".format(BankAccount.accountBalance))

        time.sleep(3)


threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print("Execution Ends")
