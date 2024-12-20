#  Decorator

# def success(x):
#     return x+1

# # print(success(10))
# successor=success
# # print(successor(20))

# # kita memiliki function yang memiliki arti yang sama yaitu success dan successor
# # selanjutnya fakta penting  bahwa kita dapat menghapus nama function antara success atau successor tanpa menghapus function itu sendiri
# del success
# print(successor(10)) # function masih ada



# function di dalam function

# def f():
#     def g():
#         print("ini function g")
#     print("ini function f")
#     g()

# f()


# example 2

# def temperatur(t):
#     def celsius2fahrenheit(x):
#         return 9*x/5+32
#     return "suhu = "+ str(celsius2fahrenheit(t))+"derajat!"

# print(temperatur(20))


# example 3

# def factorial(n):
#     """calculate the factorial of n,
#     n should be an integer and n <= 0"""
#     if n<=0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(3))


# def factorial(n):
#     """calculate the factorial of n,
#     n should be an integer and n <= 0"""
#     if type(n)==int and n>=0:
#         if n==0:
#             return 1
#         else:
#             return n*factorial(n-1)
#     else:
#         raise TypeError("n harus berupa bilangan positif atau 0")

# print(factorial(-3))





# def factorial(n):
#     def inner_factorial(n):
#         if n==0:
#             print("returning ... {}".format(n))
#             return 1
#         else:
#             ret_value=n*inner_factorial(n-1)
#             print("returning .. {}".format(ret_value))
#             return ret_value
#     if type(n)==int and n>=0:
#         return inner_factorial(n)
#     else:
#         raise TypeError("n harus bilanga positif atau 0")

# print(factorial(5))




# function returning function

# def f(x):
#     def g(y):
#         return y+x+4
#     return g

# fn=f(10)
# print(fn(20))



# polinomial
# p(x)=ax^2+bx+c

# def create_polinomial(a,b,c):
#     def polinomial(x):
#         return a*x**2+b*x+c
#     return polinomial

# p1=create_polinomial(6,3,-20)
# p2=create_polinomial(1,2,1)
# for x in range(-2, 2):
#     print("{:5d}, {:5d}, {:5d} \n".format(x,p1(x),p2(x)))

# polinomial lebih dari 2

# def create_polinomial(*a_n):
#     def polinomial(x):
#         res=0
#         for i,a in enumerate(a_n[::-1]):
#             res+=a*x**i
#         return res
#     return polinomial

# p1=create_polinomial(4)
# p2=create_polinomial(2,4)
# p3=create_polinomial(1, 2, -1, 3, 2)
# p4=create_polinomial(1, 2, 1)

# for x in range(-2,2):
#     print(x, p1(x), p2(x), p3(x), p4(x))




# simple decorator 

# def our_decor(func):
#     def function_wrap(x):
#         print("before calling "+ func.__name__)
#         func(x)
#         print("after calling "+ func.__name__)
#     return function_wrap

# def foo(x):
#     print("hi foo telah dipanggil dengan"+ str(x))

# f=our_decor(foo)
# print(f("nama saya zaenal"))
# @our_decor
# def foo(x):
#     print("hi foo telah dipanggil dengan"+ str(x))
# foo("hai")

# another example

def argument_test_natural_number(f):
    def helper(x):
        if type(x)==int and x > 0:
            return f(x)
        else:
            raise Exception("argument is not integer")
    return helper
@argument_test_natural_number
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

for i in range(1, 10):
    print(i, factorial(i))