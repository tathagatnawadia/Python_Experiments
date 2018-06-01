def isSafe(r, c, MAX_ROW, MAX_COL):
	if r < 0 or c < 0 or r >= MAX_ROW or c >= MAX_COL:
		return False
	return True

def getMaxTrav(array, row, col, MAX_ROW, MAX_COL):
	if row == 0:
		if isSafe(row, col, MAX_ROW, MAX_COL):
			return True, array[row][col]
		else:
			return False, 0
	if not isSafe(row, col, MAX_ROW, MAX_COL):
		return False, 0

	sum1 = sum2 = 0
	if isSafe(row, col, MAX_ROW, MAX_COL) and isSafe(row-1, col-1, MAX_ROW, MAX_COL):
		flag1, sum1 = getMaxTrav(array, row-1, col-1, MAX_ROW, MAX_COL)
	if isSafe(row, col, MAX_ROW, MAX_COL) and isSafe(row-1, col+1, MAX_ROW, MAX_COL):
		flag2, sum2 = getMaxTrav(array, row-1, col+1, MAX_ROW, MAX_COL)
	if isSafe(row, col, MAX_ROW, MAX_COL):
		return True, array[row][col] + max(sum1, sum2)
	else:
		return 0	

def getMax(array, MAX_ROW, MAX_COL):
	cost = []
	for i in range(MAX_COL):
		print(getMaxTrav(array, MAX_ROW-1, i, MAX_ROW, MAX_COL))
	print(cost)

array = [[0, 2, 3, 4],
		 [15, 4, 1, 7],
		 [4, 7, 5, 9],
		 [6, 8, 6, 10]]

MAX_ROW = len(array)
MAX_COL = len(array[0])

getMax(array, MAX_ROW, MAX_COL)