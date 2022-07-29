# closure

# def outerfunction(text):
#     text=text
#     def innerfunction():
#         print(text)
#     return innerfunction

# myFunction=outerfunction("hey!")

# myFunction()

import logging as lg
lg.basicConfig(filename="example.log", level=lg.INFO)

def logger(func):
    def log_func(*args):
        lg.info("Running '{}' with arguments {} ".format(func.__name__,args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y
def sub(x, y):
    return x-y

add_logger=logger(add)
sub_logger=logger(sub)

add_logger(5,7)
sub_logger(9, 5)