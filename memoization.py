def Memoize(func):
	memory = {}
	def Memory_helper(value):
		if value not in memory:
			memory[value] = func(value)
		return memory[value]
	return Memory_helper

@Memoize
def fibonacci(value):
	if value == 0:
		return 0
	elif value == 1:
		return 1
	else:
		return fibonacci(value-1) + fibonacci(value-2)

#print(fibonacci(100))

# class Memoize:
# 	"""docstring for Memoize"""
# 	def __init__(self, func):
# 		#super(Memoize, self).__init__()
# 		print("INITIALIZING DECORATOR")
# 		self.memory = {}
# 		self.func = func
# 	def __call__(self, *args):
# 		if args not in self.memory:
# 			self.memory[args] = self.func(*args)
# 		return self.memory[args]

# def fibonacci(value):
# 	if value == 0:
# 		return 0
# 	elif value == 1:
# 		return 1
# 	else:
# 		return fibonacci(value-1) + fibonacci(value-2)

# fib = Memoize(fibonacci)

for i in range(100):
	print(str(i) + " -> " + str(fibonacci(i)))