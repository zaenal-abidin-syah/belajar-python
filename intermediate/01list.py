# Lists : Ordered, mutable, allows duplicate elements

# mylist=["banana", "cherry","apple"]

# print(mylist)

# mylist2=list()#create empty list
# mylist3=[5, True, "apple"]
# print(mylist2)

# method list
# append, insert, pop, remove, clear, reverse, sort(), 

# # perbedaan method sort dan fungsi sort
# mylist=[5, 2, 7, 9, 3]
# b=mylist.sort()
# print(mylist)# merubah urutan list awal
# print(b)

# mylist2=[5, 2, 7, 9, 3]
# b=sorted(mylist)
# print(mylist2)# urutan list awal tidak berubah
# print(b)


# # operator list (+ , *)
# a=[0]*4
# print(a)
# b=[1, 2, 3, 4]
# print(a+b)




# indeks 
# mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# a=mylist[1:8:2]
# b=mylist[8:1:-2]#awal:akhir:interval
# # negative index
# c=mylist[-1:-8:-2]
# d=mylist[-8:-1:2]

# # tiada akhir / awal
# e=mylist[:8:2]#default start 0
# f=mylist[8::-2]# default end -1
# g=mylist[:8]#default interval +1

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)




# list_org=["banana","cherry", "apple"]

# # list_cpy=list_org
# # list_cpy.pop()
# # print(list_cpy)
# # print(list_org)# list awal ikut terhapus

# # solusion with copy method
# # list_cpy=list_org.copy()
# # list_cpy.pop()
# # print(list_cpy)
# # print(list_org)

# other solution
# list_cpy=list(list_org)
# list_cpy=list_org[:]






# mylist=[1, 2, 3, 4, 5, 6]
# # loop in list
# b=[i*i for i in mylist]
# print(b)








