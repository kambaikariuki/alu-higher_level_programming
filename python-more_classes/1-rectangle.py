#!/usr/bin/python3
'''Class rectangle'''


class Rectangle:
    '''Initialize width'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''Retrieving width '''
    @property
    def width(self):
        return self.width
    
    '''Setting width'''
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
    
    def height(self):
        return self.height
    
    '''Setting width'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')


