m,n,t = 5,2,4
memo = {}

def isNullState(x, y):
	if (x, y) == (0, 0):
		return True
	elif (x, y) == (m, n):
		return True
	return False

def isTargetState(x, y):
	if x == t or y == t:
		return True
	else:
		return False

def calculateWater(x, y):
	if (x, y) in memo:
		return memo[(x, y)]

	memo[(x, y)] = None
	if isTargetState(x, y):
		print("SOLUTION ", x, " ", y)
		memo[(x, y)] = True
		return True

	if isNullState(x, y):
		return None
	print(x, y)

	print(" Fill 1 :: ", end="")
	a = calculateWater(m, y) #Fill 1 
	print(" Fill 2 ::", end="")
	b = calculateWater(x, n) #Fill 2
	print(" Empty 1 :: ", end="")
	c = calculateWater(0, y) #Empty 1
	print(" Empty 2 :: ", end="")
	d = calculateWater(x, 0) #Empty 2
	e = None
	f = None
	#Transfer from 1 to 2
	if x != 0:
		print(" T 1 -> 2 :: ", end="")
		if (n-y) >= x:
			e = calculateWater(0, y + x)
		elif (n-y) < x:
			e = calculateWater(x - (n-y), n)
	#Transfer from 2 to 1
	if y != 0:
		print(" T 2 -> 1 :: ", end="")
		if (m-x) >= y:
			f = calculateWater(y + x, 0)
		elif (m-x) < y:
			f = calculateWater(m, y - (m-y))
	print(a, b, c, d, e, f)

	memo[(x, y)] = a or b or c or d or e or f
	return memo[(x, y)]


print(calculateWater(5, 0))

print(memo)