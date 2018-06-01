test_set = {6 , 2 , 11 , 1 , 9 , 14 , 13 , 4 , 18}

binary_set = {}
for n in test_set:
	ones_counter = len(str(bin(n))[2:].replace('0',''))
	if ones_counter not in binary_set.keys():
		binary_set[ones_counter] = []
	binary_set[ones_counter].append(n)

superset = []
for n in binary_set:
	superset.append(binary_set[n][0])
print(superset)


