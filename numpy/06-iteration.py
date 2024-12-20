import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
for a in arr:
  print(a)

arr = np.array([[1,2,3,4,5], [6,7,8,9,0]])
for a in arr:
  print(a)
  for b in a:
    print(b)

