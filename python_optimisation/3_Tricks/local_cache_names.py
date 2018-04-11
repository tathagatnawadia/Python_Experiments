class config:
	factor = 7.3
	threshold = 12

def normalize(numbers):
	'''Normalising a list of numbers'''
	norm  = []
	for num in numbers:
		# Can be optimised by as .threshold and .factor is a dictionary lookup before using
		if num > config.threshold:
			num /= config.factor
		norm.append(num)
	return norm

def normalize2(numbers):
	'''Normalising a list of numbers'''
	# only 1 lookup .. to see $import dis > $dis.dis(normalize2) 
	thr = config.threshold
	fact = config.factor
	norm  = []
	for num in numbers:
		if num > thr:
			num /= fact
		norm.append(num)
	return norm


if __name__ == '__main__':
	import random
	random.seed(100)
	numbers = [random.randint(5,50) for _ in range(1000)]