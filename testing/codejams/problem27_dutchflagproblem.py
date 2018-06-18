a = [0, 1, 1, 0, 2, 2, 1, 0, 1, 0, 2, 2, 0, 0]

N = len(a)

def sort(numbers, N):
	L = 0
	H = N-1

	while numbers[L] == 0:
		L = L + 1
	while numbers[H] == 2:
		H = H + 1

	M = L
	while M <= H:
		if numbers[M] == 1:
			M = M + 1
		elif numbers[M] == 0:
			numbers[M], numbers[L] = numbers[L], numbers[M]
			L = L + 1
			M = M + 1
		elif numbers[M] == 2:
			numbers[H], numbers[M] = numbers[M], numbers[H]
			H = H - 1
	print(numbers)

sort(a, N)