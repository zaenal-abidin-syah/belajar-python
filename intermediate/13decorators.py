# decorator 

# def start_end_decorator(func):
# 	def wrapper():
# 		print('start')
# 		func()
# 		print('end')
# 	return wrapper

# def print_name():
# 	print('zaenal')

# print_name=start_end_decorator(print_name)

# print_name()



# decorator function


# def start_end_decorator(func):
# 	def wrapper():
# 		print('start')
# 		func()
# 		print('end')
# 	return wrapper
# @start_end_decorator
# def print_name():
# 	print('zaenal')
# print_name()




# import functools


# def start_end_decorator(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kwargs):
# 		print('start')
# 		res=func(*args, **kwargs)
# 		print('end')
# 		return res
# 	return wrapper
# @start_end_decorator
# def add5(x):
# 	return x+5


# print(add5(10))

# print(help(add5))
# print(add5.__name__)







# import functools


# def my_decorator(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kwargs):
# 		# do ...
# 		res=func(*args, **kwargs)
# 		# do ...
# 		return res
# 	return wrapper
# @start_end_decorator
# def add5(x):
# 	return x+5


# print(add5(10))









# import functools

# def repeat(num_times):
# 	def decorator_repeat(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kwargs):
# 			for _ in range(num_times):
# 				result =func(*args, **kwargs)
# 			return result
# 		return wrapper
# 	return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
# 	print(f"hallo {name}")


# greet('zaenal')













# import functools


# def start_end_decorator(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kwargs):
# 		print('start')
# 		res=func(*args, **kwargs)
# 		print('end')
# 		return res
# 	return wrapper

# def debug(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kwargs):
# 		args_repr=[repr(a) for a in args]
# 		kwargs_repr=[f"{k}={v!r}" for k,v in kwargs.items()]
# 		signature=", ".join(args_repr+kwargs_repr)
# 		print(f"Calling {func.__name__}({signature})")
# 		result=func(*args, **kwargs)
# 		print(f"{func.__name__!r} returned {result!r}")
# 		return result
# 	return wrapper


# @debug
# @start_end_decorator
# def say_hello(name):
# 	greeting=f"hello {name}"
# 	print(greeting)
# 	return greeting

# say_hello("zaenal")
















# class


class CountCalls:
	def __init__(self, func):
		self.func=func
		self.num_calls=0
	def __call__(self, *args, **kwargs):
		self.num_calls+=1
		print(f'this is executed {self.num_calls} times')
		return self.func(*args, **kwargs)



@CountCalls
def say_hello():
	print("hello")

say_hello()




