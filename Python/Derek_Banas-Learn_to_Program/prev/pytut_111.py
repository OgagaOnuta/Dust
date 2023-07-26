#!/usr/bin/python3

class Dog:
    #  Static Variable: a FIELD created outside of METHODS
    #  i.e. the value will be shared by every OBJECT of this class
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")
    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()


main()
