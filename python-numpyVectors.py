import numpy as np

# creates data structure that is a rank 1 array. Do not use a rank 1 array.
a = np.random(5)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))

# a.shape will be equal to (5,1) 5 by 1 matrix or a column vector
a = np.random.random(5,1)
print(a)
print(a.T)
print(np.dot(a, a.T))
