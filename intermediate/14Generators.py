# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# # for i in g:
# #     print(i)

# # with next function

# # value = next(g)
# # print(value)
# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)


# # 

# # print(sum(g))

# # 

# print(sorted(g))


# #  


# def countdown(num):
#     print('Starting ...')
#     while num > 0:
#         yield num
#         num-=1

# cd=countdown(4)

# value=next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))

import sys

# menggunakan function biasa

# def firstn(n):
#     nums = []
#     num=0
#     while num < n:
#         nums.append(num)
#         num+=1
#     return nums

# print(firstn(10))
# print(sum(firstn(10)))





# menggunakan generator

# def gen_firstn(n):
#     num=0
#     while num < n:
#         yield num
#         num+=1
    

# print(sum(firstn(10)))
# print(sum(gen_firstn(10))) 
# hasilnya sama tapi di function generator kita tidak perlu membuat variable list kosong


# mengecek penggunaan memori

# print(sys.getsizeof(firstn(1000000))) # 8448728
# print(sys.getsizeof(gen_firstn(1000000))) #104



#  fibonacci

# def fibonacci(limit):
#     # 0 1 1 2 3 ....
#     a, b = 0, 1
#     while a < limit:
#         yield a 
#         a, b = b, b+a

# fib = fibonacci(30)
# for i in fib:
#     print(i)



# generator vs list comprehension

# mygenerator = (i for i in range(100000) if i%2==0)
# print(sys.getsizeof(mygenerator)) # 104


# mylist = [i for i in range(100000) if i%2==0]
# print(sys.getsizeof(mylist)) # 444376







