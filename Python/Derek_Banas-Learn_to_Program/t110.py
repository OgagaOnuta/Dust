#!/usr/bin/python3

'''
A Static Method is going to allow access without
the need to initialize a class.

They are mainly used as utility methods, or also
whenever it doesn't make sense for a real world
object to be able to perform a task but you still
need to have that method available.

If you create a field outside of any method, it is
automatically a static variable, meaning the value
of the variable will be shared by every object the
variable belongs to.
'''


class Sum:
    @staticmethod
    def getSum(*args):
        sum = 0

        for i in args:
            sum += i

        return (sum)


class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    print("Sum:", Sum.getSum(1, 2, 3, 4, 5))

    spot = Dog("Spot")
    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()


main()
