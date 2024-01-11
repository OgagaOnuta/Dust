#!/usr/bin/python3


def mult_by_2(num):
    return (num * 2)


# Assigning a function to a variable
times_two = mult_by_2

print("4 * 2 =", times_two(4))


# Passing a function as argument to another function
def do_math(func, num):
    return (func(num))


print("8 * 2 =", do_math(mult_by_2, 8))


# Returning a function dynamically
def get_func_mult_by_num(num):
    def mult_by(value):
        return (num * value)

    return (mult_by)


generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

# Embedding a function into a data structure
listOfFuncs = [times_two, generated_func]

print("5 * 9 =", listOfFuncs[1](9))
print("7 * 2 =", listOfFuncs[0](7))
