#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Represents a Square"""

    def __init__(self, size):
        """New square initialization.

        Agrs:
            size (int): size of a side of the square
        """
        self.__size = size
