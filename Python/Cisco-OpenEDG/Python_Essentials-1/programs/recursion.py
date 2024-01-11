'''
Recursion
'''


# fib_i = fib_i-1 + fib_n-2
def fib(n):
	if (n < 1):
		return (None)
	if (n < 3):
		return (1)
	
	return (fib(n - 1) + fib(n - 2))


# n! = (n-1)! * n
def factorial_function(n):
	if (n < 0):
		return (None)
	if (n < 2):
		return (1)
	
	return (n * factorial_function(n - 1))


n = int(input("Enter number: "))

print("Fibonacci", n, "=>", fib(n))
print("Factorial", n, "=>", factorial_function(n))
