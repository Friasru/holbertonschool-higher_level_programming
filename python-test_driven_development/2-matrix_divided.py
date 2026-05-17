#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    """
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    first_row_size = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if first_row_size is None:
            first_row_size = len(row)
        if len(row) != first_row_size:
            raise TypeError(
                "Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)) or \
                    isinstance(element, bool):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
