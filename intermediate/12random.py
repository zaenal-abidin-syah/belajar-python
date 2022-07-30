# random

# import random

# a=random.random() # 0 - 1 (float)
# a=random.uniform(1,9) # 1 - 9 (float)
# a=random.randint(1,9) # randint(random integer) 1 - 9 (int)
# a=random.randrange(1,10) # 1 - 9 (int) 10 tidak termasuk
# a=random.normalvariate(0,1)

# print(a)
# print(f"{a:.2f}")





# mylist=list("ABCDEFGHI")

# a=random.choice(mylist) # satu elemen random
# a=random.sample(mylist,3) # 3 elemen random yang berbeda
# a=random.choices(mylist,k=3) # 3 elemen random yang sama

# print(a)

# random.shuffle(mylist) # list acak

# print(mylist)




# seed

# random.seed(1)
# print(random.random()) # nilai tidak berubah jika diulang
# print(random.randint(1,10))

# random.seed(2) # nilai random akan sama jika parameter seednya sama
# print(random.random())
# print(random.randint(1,10))








# secrets
# import secrets

# # a=secrets.randbelow(10) # random dibawah 10s
# # a=secrets.randbits(3) # random binary
# # print(a)

# mylist=list("ABCDEFGHI")
# a=secrets.choice(mylist)
# print(a)





# numpy

# import numpy as np


# harus install dulu


# a=np.random.rand(3,3)
# print(a)












