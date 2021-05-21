#!/usr/bin/python3
'''
The 4-print_square module
This module has a funciton that prints a square
'''


def print_square(size):
    '''
    The function that prints a square with the character #
    '''
    if isinstance(size, float) is True and size < 0:
        raise TypeError('size must be an integer')

    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
