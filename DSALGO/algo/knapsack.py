def f(id, val, wt, W, n):
	putting = [[0 for i in range(W+1)] for j in range(n+1)]
	putting_items = [[[] for i in range(W+1)] for j in range(n+1)]
	print(putting)
	print(putting_items)

	for i in range(n+1):
		for w in range(W+1):
			if i == 0 or w == 0:
				# putting[i][w] = 0
				continue
			elif wt[i-1] <= w:
				score1 = val[i-1] + putting[i-1][w - wt[i-1]]
				score2 = putting[i-1][w]
				if score1 > score2:
					putting_items[i][w].append(id[i-1])
					putting_items[i][w].extend(putting_items[i-1][w - wt[i-1]])
				else:
					# Defaulting and skipping the item n
					putting_items[i][w].extend(putting_items[i-1][w])
					putting[i][w] = max(score1, score2)
			else:
				# Defaulting and skipping the item n
				putting[i][w] = putting[i-1][w]
				putting_items[i][w].extend(putting_items[i-1][w])
	print(putting)
	print(putting_items)

id = [7, 2, 13]
val = [6, 10, 12]
wt = [1, 2, 3]
W = 5
n = len(val)
f(id, val , wt , W , n)