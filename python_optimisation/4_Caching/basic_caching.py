'''
Caching - invalidation / updation is tricky
'''

def fib(n):
	if n < 2:
		return 1
	return fib(n-1) + fib(n-2)

_fib_cache = {}

def fib2(n):
	if n < 2:
		return 1
	val = _fib_cache.get(n)
	if val is None:
		_fib_cache[n] = val = fib2(n-1) + fib2(n-2)
	return val
