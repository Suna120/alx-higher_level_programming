#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    def __init__(self, size=0):
        """
        initialize the private instance attribute
        """
        self.__size = size
        if size not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """function defines area of Square"""
            return self.__size ** 2
