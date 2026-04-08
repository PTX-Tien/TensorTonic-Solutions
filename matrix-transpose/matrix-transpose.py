import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.asarray(A)
    m, n = A.shape
    temp_matrix = np.zeros((n, m))
    for i in range(n):
        temp_matrix[i, :] = A[:, i]
    return temp_matrix