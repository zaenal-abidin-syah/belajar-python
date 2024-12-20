import numpy as np

# slicing numpy array
# slicing one dimensional numpy array like slice list in a python
arr = np.array([1, 2, 3, 4, 5,6,7,8,9])

# return 2,3,4,5,6
print(arr[1:6])


# create 2 dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# arr2d[ dimensions, items ]
print(arr2d[0,1])
# slice dimension 0 and item one

# slice 2 dimensional
print(arr2d[0:1, 1:3])

# slice both rows or items
print(arr2d[0:2, 1:3])