# Functional Programming
# map(aFunction, aSequence)
# filter(aFunction, aSequence)
# reduce(aFunction, aSequence)
# lambda 
# list comprehension



# map 

# jika menggunakan list
items=[1, 2, 3, 4, 5, 6]
# newItems=[]
# for i in items:
#     newItems.append(i**2)

# print(newItems)

# menggunakan map

# function biasa
# def sqr(x):
#     return x**2
# newItems=list(map(sqr,items))

# lambda function
# newItems=list(map(lambda x:x**2, items))

# print(newItems)



# import numpy
# download numpy

# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# # def sqroot(x):
#     # return numpy.sqrt(x)

# funcs=[square, cube]# sqroot tidak ikut karena belum menginstall numpy

# for r in range(5):
#     value=map(lambda x:x(r),funcs)
#     print(list(value))




# def toUppercase(s):
#     return str(s).upper()
# def printOperator(it):
#     for i in it:
#         print(i, end=" ")
#     print('')
# s=list(map(toUppercase, "abcdefghijk"))
# printOperator(s)




# map dengan iterable arguments

# listNumber=[1, 2, 3, 4, 5]
# tupleNumber=(5, 6, 3 ,8, 4)

# mapIterator=map(lambda x,y:x*y, listNumber,tupleNumber)
# printOperator(mapIterator)








# filter

# r=list(range(4, -3, -1))

# filter x>0
# dengan for loop
# result=[]
# for x in r:
#     if x>0:
#         result.append(x)
# print(result)

# dengan  filter

# newR=filter(lambda x:x>0, r)
# print(list(newR))


# example 2

# def fun(var):
#     letter=['a','i','u','e','o']
#     if var in letter:
#         return True
#     return False
# seq=['d','a','t','a','e','r','l','a','n','g']

# print(list(filter(fun,seq)))






# reduce => harus import dari functools
# from functools import reduce
# number=range(1,5)

# jika manual
# total=0
# for num in number:
#     total+=num

# print(total)

# menggunakan reduce

# print(reduce(lambda x,y:x+y,number))

