"""
Numpy exercise 2: matrices
create a function and make use of numpy library to perform some operations
create a 3x3 matrix with values ranging from 2 to 10
"""
import numpy as np

def matrix_operations():
    # create a 3x3 matrix with values ranging from 2 to 10
    matrix = np.arange(2, 11).reshape(3, 3)
    print("Matrix: \n", matrix)

    # extract all odd numbers from the matrix
    odd_numbers = matrix[matrix % 2 != 0]
    print("Odd numbers: ", odd_numbers)

    # extract all even numbers from the matrix
    even_numbers = matrix[matrix % 2 == 0]
    print("Even numbers: ", even_numbers)

    # sum of all the elements in the matrix
    sum_elements = np.sum(matrix)
    print("Sum of all elements: ", sum_elements)

    # sum of each column
    sum_columns = np.sum(matrix, axis=0)
    print("Sum of each column: ", sum_columns)

    # sum of each row
    sum_rows = np.sum(matrix, axis=1)
    print("Sum of each row: ", sum_rows)

    # transpose of the matrix
    transpose_matrix = np.transpose(matrix)
    print("Transpose of the matrix: \n", transpose_matrix)

    # flatten the matrix
    flatten_matrix = matrix.flatten()
    print("Flatten matrix: ", flatten_matrix)

    # reshape the matrix to 2x2
    reshape_matrix = matrix.reshape(2, 2)
    print("Reshape matrix: \n", reshape_matrix)