import numpy as np

arr = np.array([1,2,3,4,5,6,7])
x = [True, True, True, False, False, False, False]
print(arr[x])
print(arr[[True, True, True, False, False, False, False]])

filtered = []

for thing in arr:
  if thing % 2 == 0:
    filtered.append(True)
  else:
    filtered.append(False)

print(arr)
print(filtered)
print(arr[filtered])

# shortcut
filtered = arr % 2 == 0
print(arr)
print(filtered)
print(arr[filtered])