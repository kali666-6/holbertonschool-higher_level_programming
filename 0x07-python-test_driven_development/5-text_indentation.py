#!/usr/bin/python3
'''
The 5-text_indentation module
This module has a funciton that indents text
'''


def text_indentation(text):
    '''
    The function that that prints My name is <first name> <last name>
    '''

    st = ''
    special = {'.', '?', ':'}

    if isinstance(text, str) is False:
        raise TypeError('text must be a string')

    for char in text:
        st += char

        if char in special:
            print(st.strip())
            print()
            st = ''

    print(st.strip(), end='')
