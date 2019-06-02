


array = [[5,24], [39,60], [15,28], [27,40], [50,90]]
ld = [1] * len(array)


for i in range(1, len(array)):
	for j in range(0, i):
		if array[j][1] > array[i][0] and ld[i] < ld[j] + 1:
			ld[i] = ld[j] + 1

print(ld)


