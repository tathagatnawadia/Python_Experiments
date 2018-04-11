'''
So the idea is to precompute get_bits for 0 to MAX_INT
This way we remove the computation part during a request
'''
def get_bits(number):
	n = 0
	while number:
		if number & 1:
			n += 1
		number >>= 1
	return n

num_bits = 16
max_value = int('1' * num_bits, 2)
_bits_cache = [get_bits(n) for n in range(max_value + 1)]

def get_bits_cached(number):
	if number > max_value:
		return get_bits(number)
	return _bits_cache[number]

def test_bits():
	cases = [
		(0, 0),
		(1, 1),
		(2, 1),
		(3, 2),
		(6, 2),
		(7, 3),
	]

	for val,n in cases:
		assert get_bits(val) == n

if __name__ == '__main__':
	test_bits()