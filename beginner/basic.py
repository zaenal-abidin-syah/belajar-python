# ini komen
# ini variable=nilai variable(berupa string, int, boolean)
a=10
b="abcd12"
c=True
# list and access list
d=[1, "dua", 3.0]
print(d[2])
print(d[0:2])#index 0-2
print(d[::-1])#interval
# Negative indexing in lists
my_list = ['p','r','o','b','e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])
# list comprehensif
pow2 = [2 ** x for x in range(10)]
print(pow2)
#string list
e="0123456789"
print(e[-1:3:-1])# index awal:batas akhir:interval
# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)
# TUPLE ==> tidak bisa diubah
f=(1, "hijk", True)
# SET ==> himpunan dalam matematika ==> nilai2 didalamnya tidak boleh sama
g={3, 8, 6, 2, 6}
print("g= ",g)
print(type(g))
# dictionary ==> key:value
h={
    1:"value",
    "key":2
}
print(h[1])# cara mengakses h[key] ==> "value"
# konversi tipe data
a=str(a)
print(type(a))# ==> <class 'str'>
# string math
a="1+4"
print(eval(a))#tidak dapat dikonvert ke int
# int(), float(), str()
# konversi set, tuple, list
i=[[1,2],[2,4],[3,6]]
j=dict(i)
print("j=",j,"type= ",type(j))
i=[1,5,3,2,7]
j=tuple(i)
print("j=",j,"type= ",type(j))
i="abcdefghi"
j=list(i)
print("j=",j,"type= ",type(j))
# print parameter ==> sep:antarobject,end:akhir == \n secara default,
print("nina","adalah","seorang","mahasiswa",sep="-",end="\n")
# output formatting
k=12
l=13
print("ini k={} dan l={}".format(k,l))
print("ini k={1} dan l={0}".format(k,l))#==>indeks
print("ini k={k} dan l={l}".format(k=k,l=l))#==> keyword arguments
# import module
import math
print("factorial 5 = ", math.factorial(5))
# math.atribute ==> mengakses atribut
# import attribute dari module
from math import factorial
print("factorial 6 =", factorial(6))
# attribute ==> mengakses atribut
import sys
print(sys.path)
# operator
# aritmatic *, /, +, -, **, //, %
a=9
a+=2 # ==> a = a + 2
# comparasion >, <, <=, >=, ==, !=, 
# logical and, or, not
# bitwise &, |, ^, ~, <<, >>
print(f"10 ={bin(10)} 14 ={bin(14)} 10 & 14 =",10&14,f"biner ={ bin(10&14)}")
print(f"10 ={bin(10)} 14 ={bin(14)} 10 | 14 =",10|14,f"biner = {bin(10|14)}")
# identify is dan is not
# membership in dan not in
# function default argument
def call(nama,ucap="selamat datang"):#ucap==>default
    return nama+ucap

print(call("agus "))
# function tuple value
def greet(*names):#menggunakan asterisk*
    for name in names:
        print("Hello", name)
greet("Monica", "Luke", "Steve", "John")
# lambda 
double = lambda x: x * 2
print(double(5))
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

# global dan local variable
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
# 






