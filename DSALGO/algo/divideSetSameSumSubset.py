def findSum(array, requirement):
	if requirement == 0:
		print(array, requirement)
		return True
	if array == None or len(array) == 0:
		return False
	for number in array:
		p = array[:]
		p.remove(number)
		if findSum(p, requirement - number) == True:
			print(number)
			return True
			break


input_list = [1, 5, 2, 9, 4, 1]
findSum(input_list, sum(input_list)/2)