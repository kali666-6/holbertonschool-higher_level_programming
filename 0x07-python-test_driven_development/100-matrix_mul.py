#!/usr/bin/python3
"""This module contains matrix_mul function"""


def matrix_mul(m_a, m_b):
    """matrix_mul: divides all elemetns of matrix by 'div'
    Args:
        m_a (list): Matrix A
        m_b (list): atrix B
    """
    result_matrix = []

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError('m_b can\'t be empty')

    for row in m_a:
        for val in row:
            if type(val) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for val in row:
            if type(val) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')

    prev_len = -1
    for row in m_a:
        row_len = len(row)
        if prev_len != -1 and prev_len != row_len:
            raise TypeError('each row of m_a must be of the same size')
        prev_len = row_len

    prev_len = -1
    for row in m_b:
        row_len = len(row)
        if prev_len != -1 and prev_len != row_len:
            raise TypeError('each row of m_b must be of the same size')
        prev_len = row_len

    ma_cols = len(m_a[0])
    mb_rows = len(m_b)
    if ma_cols != mb_rows:
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_res = []
    for i_row in range(len(m_a)):
        m_res.append([])
        for i_col in range(len(m_b[0])):
            sum = 0
            for i_eq in range(len(m_b)):
                sum += m_a[i_row][i_eq] * m_b[i_eq][i_col]
            m_res[i_row].append(sum)

    return m_res
