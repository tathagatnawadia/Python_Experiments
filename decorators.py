def f():
	def g():
		print("G")
	print("F")
	g()
f()



def a():
	print("A")
def b():
	print("B")
def c(func1, func2):
	func2()
	func1()
	print("C")
c(a,b)
c(b,a)




def foo(**kwargs):
	print(kwargs)
	print("FOOOO ...")
foo_copy = foo
foo_copy(a=[1,2,3], b={'1':'One','2':'Two'})



import math
def mathDecorator(func, number):
	'''
	This function is decorator to passed math function required 
	'''
	print("Fucntion executing is " + func.__name__)
	return func(number)
print(mathDecorator.__doc__)
print(mathDecorator(math.sin, 45))
print(mathDecorator(math.cos, 60))



def polynomial_creator(a, b, c):
	def polynomial(x):
		return a * x**2 + b*x + c
	return polynomial
p1 = polynomial_creator(2,3,-1)
p2 = polynomial_creator(8,3,1)
#Now passing value of x
print("p1 = " + str(p1(-1)))
print("p2 = " + str(p2(0)))



def our_decorator(func):
	#func->foo when the decoration happens
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper
@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))
print("We call foo before decoration:")
foo("Hi")
print("We now decorate foo with f:")
#foo = our_decorator(foo)
#print("We call foo after decoration:")
foo(42)



from random import random, randint, choice
def my_decorator(func):
	def function_wrapper(*args, **kwargs):
		print("Before calling function -- " + func.__name__)
		result = func(*args, *kwargs)
		print("RESULT = " + str(result))
		print("After calling function  -- " +func.__name__)
	return function_wrapper
random = my_decorator(random)
randint = my_decorator(randint)
choice = my_decorator(choice)
random()
randint(3, 9)
choice([4, 5, 6])



#Now we decorate a factorial function which doesn't understand negative numbers
#So we have a helper function to assist it
#We also have a counter of how many times the function calls have been made with decorators
def my_helper_decorator(func):
	def factorial_helper(x):
		factorial_helper.calls += 1
		try:
			if type(x) == int and x>0:
				return func(x)
			else:
				raise Exception("NEGATIVE FACTORIAL")
		except Exception as e:
			pass
		else:
			pass
		finally:
			pass
	factorial_helper.calls = 0
	return factorial_helper
@my_helper_decorator
def factorial(x):
	if x == 1:
		return 1
	else:
		return x * factorial(x - 1)
print("factorial has been called = " + str(factorial.calls))
print("factorial of 10 = " + str(factorial(10)))
print("factorial of -3 = " + str(factorial(-3)))
print("factorial has been called = " + str(factorial.calls))
#Total count of calls = 11 because of recursion



def call_counter(func):
	def helper(x,y):
		helper.total_calls += 1
		try:
			if type(x) == int and type(y) == int:
				helper.valid_calls += 1
				print("x=" + str(x) + ", y=" + str(y) + " " + func.__name__)
			else:
				helper.invalid_calls += 1
				raise Exception("INTEGER ONLY SUPPORTED")
		except Exception as e:
			pass
		finally:
			pass
	helper.total_calls = 0
	helper.valid_calls = 0
	helper.invalid_calls = 0
	return helper
@call_counter
def multiply(x, y):
	return x*y
@call_counter
def add(x, y):
	return x+y
@call_counter
def substract(x, y):
	return x-y
multiply(3,4)
multiply(8,3.33)
multiply(-9,4)
substract(9,2)
substract(9,3.2)
add(-1,2.3)
print("function_name \t total \t valid \t invalid")
print("multiply", multiply.total_calls, multiply.valid_calls, multiply.invalid_calls)
print("add", add.total_calls, add.valid_calls, add.invalid_calls)
print("substract", substract.total_calls, substract.valid_calls, substract.invalid_calls)



def greeting(feeling):
	def greeting_decorator(person):
		def function_wrapper(textToSay):
			if feeling == 'happy':
				print(person.__name__ + " says HAPPILY - " + person(textToSay))
			elif feeling == 'sad':
				print(person.__name__ + " says SADILY - " + person(textToSay))
			elif feeling == 'angry':
				print(person.__name__ + " says ANGRILY - " + person(textToSay))
		return function_wrapper
	return greeting_decorator
@greeting("happy")
def Mary(textToSay):
	return textToSay
Mary("i want to go to the mall")
@greeting("angry")
def Zack(textToSay):
	return textToSay
Zack("i want to go to the mall")



from greeting_decorator_manually import greeting
@greeting
def person(name, email, mobile):
	return {'name': name, 'email': email, 'mobile': mobile}
person('Tathagat', 'hellotathagat@gmail.com', '9066191461')
@greeting
def car(engine, horsepower, typres, brand, make, model):
	return "ALL"



class Fibonacci:
	'''
	This class is used to return fibonacci with remembering 
	'''
	def __init__(self):
		self.cache = {}
	def __call__(self, n):
		if n not in self.cache:
			if n == 0:
				self.cache[0] = 0
			elif n == 1:
				self.cache[1] = 1
			else:
				self.cache[n] = self.cache[n-1] + self.cache[n-2]
		return self.cache[n]
fib = Fibonacci()
for i in range(10):
	print(fib(i))




class class_decorator(object):
	"""docstring for class_decorator"""
	def __init__(self, arg):
		self.arg = arg
	def __call__(self):
		print("Decorating", self.arg.__name__)
		self.arg()
@class_decorator
def foo():
	print("inside foo()")
foo()		



		





















