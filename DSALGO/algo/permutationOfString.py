import copy

def permutation(used, available):
	if len(available) == 0:
		print(used)
	else:
		for i in range(len(available)):
			permutation(copy.deepcopy(used.d), copy.deepcopy(available.append(available[i]))

