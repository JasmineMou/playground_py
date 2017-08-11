import time
import functools



## decorating using functions
def timer_decorator(f):
	''''Output the execution time of function f.'''
	def wrapper():
		t_start = time.time()
		f()
		t_end = time.time()
		return "Execution time: {}.".format(str((t_end-t_start)))
	return wrapper

def sleep_decorator(f):
	'''Limits the speed of function called.'''
	def wrapper(*args, **kwargs):
		time.sleep(0.1)
		return f(*args, **kwargs)
	return wrapper

@sleep_decorator
@timer_decorator
def simple_func():
	l = [i for i in range(0,100)]
	return "Sum of #s in the list: {}.".format(str(sum(l)))

# print(simple_func())

# @timer_decorator, @sleep_decorator
# Sum of #s in the list: 4950.
# Execution time: 0.100306987762.

# @sleep_decorator, @timer_decorator
# Sum of #s in the list: 4950.
# Execution time: 0.000180959701538.


# reusable & chaining decorator
def tags(tag_name):
	def tags_decorator(f):
		@functools.wraps(f)
		def wrapper(text):
			return "<{0}>{1}</{0}>".format(tag_name, f(text))
		return wrapper
	return tags_decorator

@tags("div")
@tags("p")
@tags("strong")
def welcome_msg(name):
	return "Welcome, {}".format(name)

# print(welcome_msg("John"))
# <div><p><strong>Welcome, John</strong></p></div>

# print(welcome_msg.__name__, welcome_msg.__doc__, welcome_msg.__module__) 
# ('wrapper', None, '__main__'), 			without @functools.wraps
# ('welcome_msg', None, '__main__'),		with @functools.wraps, which will update the attributes of the wrapping func (wrapper) to those of the original func (welcome_msg).



## decorating using class
class decorator_class(object):
	def __init__(self, f):
		self.f = f 

	def __call__(self):
		print("Decorating {}".format(self.f.__name__))
		return self.f()

@decorator_class
def simple_func2():
	l = [i for i in range(0,100)]
	return "Sum of #s in the list: {}.".format(str(sum(l)))

# print(simple_func2())	

class memoize_decorator:
	def __init__(self,f):
		self.f = f
		self.memo = {}

	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

@memoize_decorator
def fib(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fib(n-1) + fib(n-2)

# print(fib(5))



## staticmethod
class A(object):
	def foo(self,x):
		print("foo({},{})".format(self,x))

	@classmethod
	def foo_classmethod(cls,x):
		'''the class of object instance is implicitly passed as the first arg instead of self'''
		print("foo_class({},{})".format(cls,x))

	@staticmethod
	def foo_staticmethod(x):
		'''Neither self (the object instance) or the class is implicitly passed as the first argument. Behave like plain functions except you can call them from an instance or the class'''
		print("foo_staticmethod({})".format(x))
a=A()
a.foo(1)
a.foo_classmethod(1)
a.foo_staticmethod(1)
A.foo_staticmethod("One")
# foo(<__main__.A object at 0x104c20c10>,1)
# foo_class(<class '__main__.A'>,1)
# foo_staticmethod(1)
# foo_staticmethod(One)

## property method
## https://stackoverflow.com/a/44166208/2687773




