# mytuple=("halo", 28, "bola")
# print(mytuple)


# mytuple=("halo")
# print(type(mytuple))
# # type string
# mytuple=("halo",)# tambahkan , koma agar typenya tuple
# print(type(mytuple))



# mytuple=tuple(["halo", 28, "bola"])
# can access index but cant change
# print(mytuple[2])
# mytuple[2]="change"



# mytuple=tuple(["halo", 28, "bola"])
#  can use for
# for i in mytuple:
#     print(i)

# can used selection
# if "halo" in mytuple:
#     print("yes")
# else:
#     print("no")






# my_tuple=('a','p','p','l','e')
# # print(len(my_tuple))

# # method tuple
# # count, index
# # print(my_tuple.count('p'))# mencari jumlah dari suatu elemen
# # print(my_tuple.index('l'))# mencari indeks dari element, note hanya 1 elemen

# # merubah ke list dan sebaliknya
# # mylist=list(my_tuple)
# # print(mylist)
# # my_tuple=tuple(mylist)
# # print(my_tuple)





# acces index tuple
# a=(1, 2, 3, 4, 5, 6, 7, 8, 9)
# b=a[2:5]
# print(b)


# # unpacking
# my_tuple="halo", 10, "dunia"
# a, b, c =my_tuple # jumah variable harus sama dengan jumlah elemen tuple
# print(a, b, c)


# my_tuple=(0, 1, 2, 3, 4)
# i1, *i2, i3=my_tuple
# print(i1)
# print(i2)
# print(i3)



# tuple menghabiskan lebih sedikit resource dibanding list
# import sys
# my_list=[0, 1, 2, "hello", True]
# my_tuple=(0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list),"bytes")
# print(sys.getsizeof(my_tuple),"bytes")

# waktu proses lebih cepat tuple dibanding list
# import timeit
# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
