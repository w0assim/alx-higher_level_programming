#!/usr/bin/python3
"""s"""


class Square:
    """s"""
    def __init__(self, size=0):
        """s"""
        self.size = size

    @property
    def size(self):
        """s"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sss"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """s"""
        return (self.__size * self.__size)
