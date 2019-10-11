import numpy as np

def cumsum(A):
    #YOUR CODE

    result = np.cumsum(A, axis=1)
    return result