'''
Lots of small python objects can cause problems
python objects store attributes in a dictionary called __dict__
Dictionaries are optimised for speed but are 1/3 empty
This can cause an overhead
Using __slots__ removes __dict__, downside being 
attributes can't be added to object
'''

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		cls_name = self.__class__.__name__
		return f'{cls_name}({self.x!r}, {self.y!r})'

class Point2:
	__slots__ = ['x', 'y']
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		cls_name = self.__class__.__name__
		return f'{cls_name}({self.x!r}, {self.y!r})'

if __name__ == '__main__':
	def alloc_points(n):
		return [Point(i, i) for i in range(n)]

	def alloc_points2(n):
		return [Point2(i, i) for i in range(n)]

	n = 1_000_000
	points = alloc_points(n)
	points2 = alloc_points2(n)

'''
import sys
sys.getsizeof(points) == sys.getsizeof(points2) cause they store memory of references

pip install memory_profiler 
%load_ext memory_profiler
%mprun -f alloc_points alloc_points(n)
%mprun -f alloc_points2 alloc_points2(n)
'''
