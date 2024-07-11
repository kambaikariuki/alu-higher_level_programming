#!/usr/bin/python3
'''
Class square defined by instantiation with optional size
'''


class Square:
    '''
    Initialize class square
    '''
    @property
    def __init__(self, size=0):
        self.size = size
    '''
    Returns area of square 
    '''
    def area(self):
        return (self.size * self.size)
    
    def size(self):
          return self.size
    
    @size.setter
    def size(self, value):
        if type(value) != int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.size = value
