#!/usr/bin/python3
'''
The 0-add_integer module
This module has a function that adds integers
'''


def add_integer(a, b=98):
    '''
    The function for adding 2 integers
    '''
    if isinstance(a, int) is False and isinstance(a, float) is False or a != a:
        raise TypeError('a must be an integer')
    if isinstance(b, int) is False and isinstance(b, float) is False or b != b:
        raise TypeError('b must be an integer')
    if a == float('inf'):
        a = 0
    if b == float('inf'):
        b = 0
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
