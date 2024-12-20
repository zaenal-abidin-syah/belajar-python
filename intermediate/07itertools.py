#  Itertools : product, permutations, combination, accumulate, groupby, and infinite iterator



# product

# from itertools import product

# a = [1, 2]
# b = [3, 4]
# # p=product(a,b)

# p=product(a,b, repeat=2)

# print(list(p))





# permutations
# from itertools import permutations
# a=[1,2,3]
# perm=permutations(a)
# perm=permutations(a,2)

# print(list(perm))





# combination

# from itertools import combinations, combinations_with_replacement as combreplace

# a=[1,2,3,4]
# comb=combinations(a, 2)
# print(list(comb))
# print(list(combreplace(a,2)))






# accumulate
# from itertools import accumulate
# import operator

# a=[1, 2, 3, 4]

# acc=accumulate(a)
# acc=accumulate(a, func=max)

# print(a)
# print(list(acc))

# b=['a','b','c']
# print(list(accumulate(b)))










# groupby

# from itertools import groupby


# def smaller_than_3(x):
    # return x<3

# a=[1,2,3,4]
# gb=groupby(a, key=smaller_than_3)

# for key, value in gb:
#     print(key, list(value))


# a=[1,2,3,4]
# gb=groupby(a, key=lambda x:x<3)

# for key, value in gb:
#     print(key, list(value))


# person=[
#     {"nama":"tim","age":25},
#     {"nama":"dan","age":25},
#     {"nama":"lisa","age":27},
#     {"nama":"claire","age":28},
# ]

# gb=groupby(person, key=lambda x:x["age"])

# for key, value in gb:
#     print(key, list(value))




from itertools import count, cycle, repeat

# for i in count(10):
#     print(i)
#     if i==20:
#         break

# a=[1, 2, 3]
# for i in cycle(a):
#     print(i)

for i in repeat(1, 4): # limit 4
    print(i)
