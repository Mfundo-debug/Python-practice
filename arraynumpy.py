"""
use numpy library to compute the determinant of a matrix
"""
def determinant_of_matrix(n, a):
    import numpy as np
    return round(numpy.linalg.det(a),2)
if __name__ == '__main__':
    n = int(input())
    a = np.array([input().split() for _ in range(n)], float)
    print(determinant_of_matrix(n, a))