#!/usr/bin/python3

"""s"""


class Square:
    """s"""
    def __init__(self, size=0):
        """s"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """s"""
         return (self.__size * self.__size)
