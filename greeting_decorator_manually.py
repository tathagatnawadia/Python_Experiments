from functools import wraps
def greeting(func):
	@wraps(func)
	def function_wrapper(*args):
		""" function_wrapper documentation """
		print("Hi, from " + func.__name__ + " which returns = ")
		print(func(*args))
	#overwriting everything for the function_wrapper
	return function_wrapper

