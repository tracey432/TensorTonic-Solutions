import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    r, c = len(A), len(A[0])
    answer = []
    for i in range(c):
        temp = []
        for j in range(r):
            temp.append(A[j][i])
        answer.append(temp)
    return np.asarray(answer)