def findMin(coin_list, target):
	if target == 0:
		print(target)
		return True, 0
	number_of_coins = 999999
	for coin in coin_list:
		if coin <= target:
			reached, x = findMin(coin_list, target-coin)
			if reached == True and x < number_of_coins:
				number_of_coins = x

	if number_of_coins != 999999:
		return True, number_of_coins + 1
	else:
		return False, number_of_coins


def findMinDynamic(coin_list, target):
	dp = [[0 for i in range(target+1)] for j in range(len(coin_list)+1)]
	for i in range(1, len(coin_list)+1):
		for j in range(1, target+1):
			if j % coin_list[i-1] == 0:
				for ite in range(1, j/coi)

		print(dp[i])

coin_list = [9, 6, 5, 1]

target = 11

print(findMinDynamic(coin_list, target))