#  membuat function iterator sendiri
#  function yang tidak menggunakan return melainkan menggunakan yield

# def myGenerator():
#     print("first Item")
#     yield 10

#     print("second item")
#     yield 20

#     print("last item")
#     yield 30

# # this is generator function
# gen=myGenerator()

# print(next(gen)) # mengembalikan nilai 10
# print(next(gen)) # mengembalikan nilai 20
# print(next(gen)) # mengembalikan nilai 10
# print(next(gen)) # error


#  perbedaan yield dengan return, yield mengembalikan nilai dan menghentikan sementara eksekusi ketika sedang maintain 
# return, mengembalikan nilai dan menghentikan function



# def myGenerator():
#     print("first Item")
#     yield 10

#     print("second item")
#     yield 20
#     return

#     print("last item")
#     yield 30

# # this is generator function
# gen=myGenerator()

# print(next(gen)) # mengembalikan nilai 10
# print(next(gen)) # mengembalikan nilai 20
# print(next(gen)) # error karena ada return di sebelmnya




# for loop in function generator



# def getSequenceUpTo(x):
#     for i in range(x):
#         yield i

# seq=getSequenceUpTo(3)

# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq)) # error max 3




#  kasus fibonaci

def fibonaci(max):
    # nilai awal
    a,b=0,1
    while a<max:
        yield a
        a,b=b,a+b

fi=fibonaci(5)
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))# error
