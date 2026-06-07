#!/usr/bin/python3
"""Module that generates Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        new_row = [1]
        for j in range(len(triangle[i-1]) - 1):
            new_row.append(triangle[i-1][j] + triangle[i-1][j+1])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
