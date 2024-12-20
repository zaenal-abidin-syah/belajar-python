#  Dictionaries : Key-value pairs, unordered, mutable

# mydict={
#     "nama":"zaenal",
#     "age":20,
#     "city":"bojonegoro"
# }

# dictionaries function
# mydict2=dict(nama="rizki", age=19, city="bojonegoro")
# print(mydict2)


# aksess value
# value=mydict['nama']
# print(value)
# # create
# mydict["email"]="zaens@gmail.com"
# print(mydict)




# mydict={
#     "nama":"zaenal",
#     "age":20,
#     "city":"bojonegoro"
# }

# delete
# del mydict["nama"]

# # method
# mydict.pop("age")
# mydict.popitem()#item terakhir
# print(mydict)

# if "nama" in mydict:
#     print(mydict["nama"])

# # or with try except

# try:
#     print(mydict["lastname"])
# except:
#     print("error")


# for key in mydict.keys():
#     print(key)


# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

# print(mydict.keys())
# print(mydict.values())




# mydict={
#     "nama":"zaenal",
#     "age":20,
#     "city":"bojonegoro"
# }
# copy
# mydict_cpy=mydict
# mydict_cpy["lastname"]="abidin"
# print(mydict_cpy)
# print(mydict)# dict awal juga ikut berubah


# solution
# mydict_cpy=mydict.copy()
# mydict_cpy["lastname"]="abidin"
# print(mydict_cpy)
# print(mydict)

# mydict_cpy=dict(mydict)
# mydict_cpy["lastname"]="abidin"
# print(mydict_cpy)
# print(mydict)



# update


# my_dict={
#     "nama":"zaenal",
#     "age":20,
#     "city":"bojonegoro"
# }
# my_dict_2=dict(nama="Rizki", age=19, city="bojonegoro")
# my_dict.update(my_dict_2)
# print(my_dict)



# my_dict={3:9,6:36,8:81}
# print(my_dict)
# value=my_dict[3]# dont have index 
# print(value)

# # tuple dalam dict
# my_tuple=(6, 7)
# my_dict={my_tuple:15}
# print(my_dict)

# list dalam dict tidak bisa karena key dalam dict adalah tidak bisa diubah berbeda dengan list yang bisa diubah
