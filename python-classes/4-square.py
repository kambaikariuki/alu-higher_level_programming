#!/usr/bin/python3
'''
Class square defined by instantiation with optional size
'''


class Square:
    '''
    Class square defined by instantiation with optional size
    '''
    def __init__(self, size=0):
        if type(size) != int:
                raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size
    '''
    Returns area of square 
    '''
    def area(self):
        return (self.__size * self.__size)
    '''
    Getting size
    '''
    def size(self):
          return self.__size
    '''
    Setting new size
    '''
    def size(self, value):
        if type(value) != int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value
