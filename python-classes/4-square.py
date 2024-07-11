#!/usr/bin/python3
'''
Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it
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
