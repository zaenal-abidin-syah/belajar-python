import numpy as np

# create array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# create array use arrange
arr = np.arange(1, 6)
print(arr)
# create array use arrange step
arr = np.arange(1, 6, 2)
print(arr)

# create array zero
arr = np.zeros(5)
print(arr)

# create multidimensional zero
arr = np.zeros((3, 4))
# explain
# arr = [[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]]
print(arr)

# create array one
arr = np.ones(5)
print(arr)

# create array full and explain
arr = np.full(5, 5)
# explain
# arr = [5, 5, 5, 5, 5]
print(arr)

# create multidimensional full
arr = np.full((3, 4), 5)
# explain
# arr = [[5, 5, 5, 5],
#        [5, 5, 5, 5],
#        [5, 5, 5, 5]]
print(arr)

# convert array to numpy
dataList = [1,2,3,4,5]
arr = np.array(dataList)
print(arr)