#!/usr/bin/python3
'''
The 3-say_my_name module
This module has a funciton that says a name
'''


def say_my_name(first_name, last_name=""):
    '''
    The function that that prints My name is <first name> <last name>
    '''
    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')
    if isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
