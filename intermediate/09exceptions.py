#  Error and Exceptions

# a=5
# print(a)) # SyntaxEror = invalid syntax

# a=5 + "10" # TypeError = unsuported operand

# import somemudule # ModuleNotFounError

# b=c # NameError = name c is not defined

# f=open('somefile.txt') # FileNotFoundError

# a=[1,2,3]
# a.remove(4) # ValueError
# a[4] # IndexError

# my_dict={'name':'zaenal'}
# my_dict['age'] # KeyError


# x=-5
# if x<0:
#     raise Exception('x should be positive')


# x=5
# assert (x>=0),"x is not positive"


# try:
#     a=5/0 # ZeroDivisionError
# except :
#     print('an error happened')



# try:
#     a=5/0 # ZeroDivisionError
# except Exception as e:
#     print(e)



# try:
#     a=5/0 # ZeroDivisionError
#     b=a+"10"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up ...')




# class error
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, massage, value):
        self.massage=massage
        self.value=value

def test_value(x):
    if x>100:
        raise ValueTooHighError("value is to high")
    if x<5:
        raise ValueTooSmallError("value is too small", x)

# test_value(200)
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.massage, e.value)
