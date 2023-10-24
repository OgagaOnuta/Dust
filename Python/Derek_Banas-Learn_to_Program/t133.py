#!/usr/bin/python3

'''
A GENERATOR function is going to return a result generator whenever
you call it and you would be able to spend or resume during execution
to create results over time rather than all at once.

We mainly use Generators when we want to get a very large result set but
we don't want to slow down our program by creating the result all at once
'''


def isprime(num):
    for i in range(2, num):
        if ((num % i) == 0):
            return (False)

    return (True)


def gen_primes(max_number):
    for num1 in range(2, max_number):
        if (isprime(num1)):
            # Generator keyword
            yield (num1)


prime = gen_primes(50)

print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
