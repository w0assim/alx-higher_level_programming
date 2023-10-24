#!/usr/bin/python3
"""s"""


class Square:
    """s"""
    def __init__(self, size):
        """s"""
        self.size = size
    @property
    def size(self):
        """s"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """s"""
         if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """s"""
        return (self.__size * self.__size)

    def my_print(self):
        """s"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
