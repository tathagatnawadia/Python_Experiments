def findMax(string, i, j):
	if i == j:
		return 1
	if i > j:
		return 0
	if string[i] == string[j]:
		return max(2 + findMax(string, i+1, j-1),
			findMax(string, i+1, j),
			findMax(string, i, j-1))
	else:
		return max(findMax(string, i+1, j-1),
			findMax(string, i+1, j),
			findMax(string, i, j-1))



string = "GEEKSFORGEEKS"
print(findMax(string, 0, len(string)-1))