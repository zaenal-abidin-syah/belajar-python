import numpy as np

# shape one dimensional
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.shape)
# shape 2 dimensional
arr = np.array([[1,2,3,4],[4,5,6,8],[7,8
,9, 2]])
print(arr.shape)

# reshape 2 d
arr = np.array([0,1,2,3,4,5,6,7,8
,9])
print(arr.shape)
arr = arr.reshape(2,5)
print(arr)
print(arr.shape)

# reshape 3 d
arr = np.array([0,1,2,3,4,5,6,7
,8,9,10,11,12,13,14,15])
print(arr.shape)
arr = arr.reshape(2,2,4)
print(arr)
print(arr.shape)

# flaten to 1 d
arr = arr.reshape(-1)
print(arr)
print(arr.shape)