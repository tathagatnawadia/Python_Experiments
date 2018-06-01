'''Optimising fucntion calls by 
	1. inline-ing 
	2. Unneccesary use of properties (setters-getters)
'''

# Empty function call %timeit noop() to check
def noop():
	pass

def abs_even(number):
	if number%2 == 0 and number > 0:
		return -number
	else:
		return number

def fix_numbers(numbers):
	return [abs_even(number) for number in numbers]

# Now removing the need to call abs_even and inlin-ing the logic
def fix_numbers2(numbers):
	fixed = []
	append = fixed.append

	for number in numbers:
		fixed_number = -number if number%2 == 0 and number<0 else number
		append(fixed_number)
	return fixed

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Point2:
	def __init__(self, x, y):
		self._x = x
		self._y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError(type(value))
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError(type(value))
		self._y = value

'''
In [39]: %timeit Point(1,2)
613 ns ± 7.89 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [40]: %timeit Point2(1,2)
619 ns ± 12.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [41]: p1 = Point(1,2)

In [42]: p2 = Point2(1,2)

In [43]: %timeit p1.x
59 ns ± 0.628 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [44]: %timeit p2.x
195 ns ± 1.75 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
'''

if __name__ == '__main__':
	import random 
	random.seed(100)

	numbers = [random.randint(-20,20) for _ in range(1000)]

