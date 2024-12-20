import numpy as np

# sqrt, menghitung akar kuadrat
arr = np.array([1,4,9,16,25])

print(np.sqrt(arr))

# absolut value
arr = np.array([-2, -3, -1, 0, 4, 6, 8])
# abs = absolut
print(np.abs(arr))
print(np.absolute(arr))

# exponentials
print(np.exp(arr))

# min / max
arr = np.array([1, 2, 3, 4, 5])
print(np.min(arr))
print(np.max(arr))

# sing negative or positif
arr = np.array([-1, -2, -3, -4, -5, 0, 1, 3, 5])
print(np.sign(arr))

# trig sin cos log
arr = np.array([ 1, 3, 4, 5])

print(np.sin(arr))
print(np.cos(arr))
print(np.log(arr))