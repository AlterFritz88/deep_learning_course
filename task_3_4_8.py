import numpy as np

def no_numpy_scalar(v1, v2):
    #YOUR CODE: please do not use numpy

    result = sum([x*y for x, y in zip(v1, v2)])
    return result

def numpy_scalar (v1, v2):
    #YOUR CODE

    result = np.dot(v1, v2)
    return result


x = [1,2,3]
y = [1,2, 3]


mx = np.array(x)
my = np.array(y)

print(no_numpy_scalar(x, y))
print(numpy_scalar(mx, my))