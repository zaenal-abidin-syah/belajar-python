# mystring="   hello world   "
# mystring=mystring.strip() # agar seperti kalimat pada umumnya
# print(mystring)


# mystring="hello world"
# print(mystring.lower()) # huruf kecil
# print(mystring.upper()) # huruf besar

# print(mystring.startswith("h")) # mengecek karakter pertama
# print(mystring.startswith("hello")) # mengecek karakter pertama

# print(mystring.endswith("d")) # mengecek karakter pertama
# print(mystring.endswith("world")) # mengecek karakter pertama

# print(mystring.find("o")) # mencari indeks dari karakter
# print(mystring.find("lo")) # mencari indeks dari substring

# print(mystring.count('o')) # menghitung berapa kali muncul karakter

# print(mystring.replace('world', 'dunia'))



# mystring='how are you doing'
# mylist=mystring.split() # default pemisah adalah space
# print(mylist)
# newstring=" ".join(mylist)# pemisah space
# print(newstring)


# # time
# from timeit import default_timer as timer
# mylist=['a']*10000000

# # bad
# start=timer()
# mystring=''
# for i in mylist:
#     mystring+=i
# stop=timer()
# print(stop-start)

# # good
# start=timer()
# mystring="".join(mylist)
# stop=timer()
# print(stop-start)




#  %, format, fstring

# var = 3.141123
# mystring="the variable is %.2f" % var # %s, %d, %f, %.2f=> angka dibelkang koma
# print(mystring)


# var = 3.14672533
# var2 = 6
# mystring="the variable is {:.2f} and {}".format(var, var2)
# print(mystring)


# var = 3.14672533
# var2 = 6
# # mystring=f"the variable is {var:.2f} and {var2:5d}"
# mystring=f"the variable is {var*4:.2f} and {var2*3:5d}"
# print(mystring)





