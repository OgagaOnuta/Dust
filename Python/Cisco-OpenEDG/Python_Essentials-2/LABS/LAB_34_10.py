'''
Triangle
'''

from LAB_34_9 import Point
import math


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        result, j = 0, 1
        length = len(self.__vertices)

        for i in range(length):
            if (j == length):
                j = 0

            result += self.__vertices[i].distance_from_point(self.__vertices[j])
            j += 1

        return (result)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))

print(triangle.perimeter())
