def maxIncreasingSubsequence(numbers):
	length = len(numbers)
	ref = [1 for i in range(length)]

	for i in range(1, length):
		for j in range(0, i):
			if numbers[i] > numbers[j] and ref[i] < ref[j] + 1:
				ref[i] = ref[j] + 1
		print(numbers)
		print(ref) 


maxIncreasingSubsequence([50, 3, 10, 7, 90, 40, 80])