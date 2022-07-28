import pickle as p

# pickle

# f=open("pickled.txt","wb")
# dct={
#     "nama":"Zaenal",
#     "age":23,
#     "gender":"male",
#     "marks":75
# }
# p.dump(dct, f)
# f.close()

# unpickle


# f=open("pickled.txt","rb")
# dct={
#     "nama":"Zaenal",
#     "age":23,
#     "gender":"male",
#     "marks":75
# }
# d=p.load(f)
# print(d)
# f.close()

# 




# dumps / loads

# dumps

# from pickle import dumps as d
# dct={
#     "nama":"Zaenal",
#     "age":23,
#     "gender":"male",
#     "marks":75
# }
# dctstring=d(dct)
# print(dctstring)

# from pickle import loads as l
# dctload=l(dctstring)
# print(dctload)



# def storeData():
#     # initializing data to be stored in db
#     Zaenal={"key":"Zaenal","name":"zaenal abidin", "age":20,"pay":40000}
#     Rizki={"key":"Rizki","name":"rizki alamsyah", "age":19,"pay":30000}

#     # database
#     db={}
#     db["Zaenal"]=Zaenal
#     db["Rizki"]=Rizki

#     # example to use binary mode
#     dbfile=open("examplepickle","ab")

#     # source destination
#     p.dump(db, dbfile)
#     dbfile.close()

# def loadData():
#     # for reading also binary mode is importen
#     dbfile=open("examplepickle","rb")

#     db=p.load(dbfile)
#     for keys in db:
#         print(keys,"=>",db[keys])
#     dbfile.close

# storeData()
# loadData()
