import numpy as np



# view
print("VIEW : ++++++++++++++++++++++++++++++")
arr = np.array([1,2,3,4,5])
arr2 = arr.view()

print(arr)
print(arr2)

arr[0] = 9

print(arr)
print(arr2)

# nilai arr2 mengikuti arr

print("COPY : ++++++++++++++++++++++++++++++")
arr = np.array([1,2,3,4,5])

arr2 = arr.copy()

print(arr)
print(arr2)

arr[0] = 9

print(arr)
print(arr2)