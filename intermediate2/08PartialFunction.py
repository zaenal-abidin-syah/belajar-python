def power(base, exponent):
    print("{} to the power {} = {}".format(base, exponent, base**exponent))
    return base**exponent

# def square(base):
    # return power(base, 2)


# def cube(base):
    # return power(base, 3)

# print(square(4))
# print(cube(4))
# misalkan kita ingin print square atau cube function sebanyak banyaknya, 1000 misalnya maka function power akan dipanggil 1000 kali juga

# solusi adalah dengan menggunakan functools.partial
from functools import partial

# square=partial(power, exponent=2)
# cube=partial(power, exponent=3)

# print(square(3))
# print(cube(3))


# example 2

# from functools import partial
# a normal function
# def f(a, b, c, x):
#     return 1000*a+100*b+10*c+x

# g=partial(f,3,1,4)
# print(g(10))

# a normal function
# def add(a, b, c):
#     return 100*a+10*b+c
# add_part=partial(add, c=2, b=1)
# print(add_part(3))



# def operator(op,x,y):
#     if op=="tambah":
#         return x+y
#     elif op=="kurang":
#         return x-y
#     elif op=="kali":
#         return x*y
#     elif op=="bagi":
#         return x/y


# tambah=partial(operator,"tambah")
# kurang=partial(operator,"kurang")
# kali=partial(operator,"kali")
# bagi=partial(operator,"bagi")

# print(tambah(4, 6))
# print(kurang(7, 9))
# print(kali(5,6))
# print(bagi(90,5))