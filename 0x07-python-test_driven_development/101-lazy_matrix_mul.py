#!/usr/bin/python3
"""This module contains lazy_matrix_mul function"""


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul: Multiplies 2 matrices
    Args:
        m_a (list): Matrix A
        m_b (list): Matrix B
    """
    import numpy

    return numpy.matmul(m_a, m_b)
