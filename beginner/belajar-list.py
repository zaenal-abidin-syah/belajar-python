"""
belajar list
"""
from functools import reduce


data_list = []
# data_list = list()

data_list.append(1)
data_list.append(2)
data_list.append(3)
data_list.append(4)
print(data_list)


data_list.extend([5,6,7])
print(data_list)


data_list.insert(2, "insert")
print(data_list)

data_list.pop()
print(data_list)

ind = data_list.index("insert")
print(ind)


data_list.remove("insert")
print(data_list)




data_list.reverse()
print(data_list)

data_list.sort()
print(data_list)


new_list = list(map(lambda x:x**2, data_list))
print(new_list)


new_list = list(filter(lambda x:x>2, data_list))
print(new_list)


new_list = reduce(lambda x, y:x+y, data_list)
print(new_list)


data_list.clear()
print(data_list)
