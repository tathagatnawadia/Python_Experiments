'''
Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {30, 20, 110, 1, 100}
Output : 99
Explanation : The maximum difference is between 100 and 2.
'''

def max_difference(arr):
	max_diff = arr[0] - arr[1]
	min_index = 0

	for i in range(1, len(arr)):
		if arr[i] < arr[min_index]:
			min_index = i
		if max_diff < arr[i] - arr[min_index]:
			max_diff = arr[i] - arr[min_index]

	return max_diff



arr = [ ([30, 20, 110, 1, 33, 100], 99),
		([30, 20, 190, 1, 33, 100], 170),
		([-30, 20, 110, 1, 33, 100], 140)]

for i in arr:
	assert max_difference(i[0]) == i[1]