class MyList:
	def __init__(self, it):
		self._data = list(it)
		self._app = {}

	def __getattr__(self, name):

		attr = object.__getattribute__(self._data, name)
		print(attr)
		if callable(attr):
			def wrapper(*a, **kw):
				print("Before ..")
				result = attr(*a, **kw)
				print("After ..")
				return result
			return wrapper
		return attr


mylist = MyList(range(4))
print(mylist)


class Wrapper(object):
	''' Wrapper class that provides proxy access to an instance of some internal instance '''
	__wraps__ = None
	__ignore__ = "class mro new init setattr getattr getattribute"

	def __init__(self, obj):
		if self.__wraps__ is None:
			raise TypeError("base class Wrapper not instantiated")
		elif isinstance(obj, self.__wraps__):
			self._obj = obj
		else:
			raise ValueError("wrapped object must be of %s" % self.__wraps__)

	def __getattr__(self, name):
		return getattr(self._obj, name)

	