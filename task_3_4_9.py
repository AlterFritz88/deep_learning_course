import numpy as np
def diag_2k(a):
    #YOUR CODE
    diag = np.diag(a)
    result = sum([x for x in diag if x % 2 == 0])
    return result

matrix = [[1,2,3],
          [4,4,4],
          [6,6,6]]

print(diag_2k(matrix))