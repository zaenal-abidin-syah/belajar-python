# membuat list berdasarkan list sebelumnya
#  cara panjang
# fruits=["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# cara pendek
# fruits=["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[each_fruit for each_fruit in fruits if "a" in each_fruit]
# print(newlist)


# h_letter=[]

# for letter in "human":
#     h_letter.append(letter)

# print(h_letter)

#  or with list comprehension
# h_letter=[letter for letter in "human"]
# print(h_letter)

# number_list=[x for x in range(20) if x%2!=0]
# print(number_list)

# obj=["even" if i%2==0 else "odd" for i in range(20)]
# print(obj)

# obj=["even" if i%2==0 else "odd" for i in range(20)]
# print(obj)

#  array = [ bagian1  bagian2  ]
#  bagian 1 biasanaya berisi hasil dari bagian 2 yang akan menjadi elemen dari array, ada juga pengkondisian terhadap hasil
# sementara bagian 2 bisa berisi pengulangan dan pengkondisian dari object iterable sebelumnya



#  list comprehension in function

# def double(x):
#     return x*2
# x=[double(x) for x in range(10)]
# print(x)


# set and dictionary comprehension
# set and dictionary comprehension ==> tidak ada duplikat

# text="life yah, finds away, in a great indeed"
#  if use array
# unique_vocal=[each_letter for each_letter in text if each_letter in "aiueo"]
# result = ['i', 'e', 'a', 'i', 'a', 'a', 'i', 'a', 'e', 'a', 'i', 'e', 'e']


# if use set
# unique_vocal={each_letter for each_letter in text if each_letter in "aiueo"}
#  result = {'a', 'e', 'i'}
# print(unique_vocal)

# if use dictionaries
# squares={i:i*i for i in range(10)}
# print(squares)


