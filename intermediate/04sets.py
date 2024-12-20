# myset={1,2,3,8,2,3,1,6,5} # hasilnya akan berurutan dan tidak ada duplikat
# print(myset)

# myset=set([1,3,2,4,7,5])
# mysetstr=set("hallo")
# print(myset)
# print(mysetstr)

# myset={}# tidak boleh karena typenya dict bukan set
# print(type(myset))



# mutable

# myset=set()
# myset.add(2)
# myset.add(7)
# myset.add(1)
# print(myset)
# myset.remove(1)
# myset.remove(7)# menggunakan method remove, jika item yang ingin diremove tidak ada di dalam tipe data set maka akan error, gunakan discard
# myset.discard(9)


# myset={1,2,3}
# print(myset.pop()) # 1 akan terhapus
# for i in myset:
    # print(i)
# if 1 in myset:
    # print("yes")





# set jika dalam matematika seperti himpunan

# odds={1,3,5,7,9}
# evens={0,2,4,6,8}
# prima={2,3,5,7}

# print(odds.union(evens)) # gabungan 
# print((odds.intersection(prima))) #irisan

# print(odds.difference(prima))# selisih
# print(odds - prima) # selisih dengan operator -
# print(odds.symmetric_difference(prima)) # (odds-prime) and (prime-odds)


# update == mengupdate element
# odds.update(prima) # gabungan 
# odds.intersection_update(prima) #irisan
# odds.difference_update(prima)# selisih
# odds.symmetric_difference_update(prima)
# print(odds)

# a= {0,2,4,6,8}
# b={2}
# c={3}

# is
# print(b.issubset(a)) # a himpunan bagian dari b
# print(a.issuperset(b)) # b bagian dari himpunan a

# print(a.isdisjoint(b)) # akan true jika tidak ada irisan
# print(a.isdisjoint(c))






# copy set

# a={1,2,3,4,5}
# b=a
# b.add(9)
# print(a,b)# a juga ikut berubah

# solusi
# a={1,2,3,4,5}
# b=a.copy()
# b.add(9)
# print(a,b)

# a={1,2,3,4,5}
# b=set(a)
# b.add(9)
# print(a,b) # a tidak ikut berubah


# a=frozenset([1,2,3,4,5]) # tidak bisa diubah
# a.add(2) #err
# a.remove(3) #err
# print(a)