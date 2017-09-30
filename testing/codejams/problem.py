T = int(input())
test_counter = 1
election_result = []
while test_counter <= T:
	test_counter = test_counter + 1
	N,K = list(map(int, input().split()))
	city_counter = 1
	developed = []
	devloping = []
	while city_counter <= N:
		city_counter = city_counter + 1
		type_of_city, population = list(map(int, input().split()))
		if type_of_city == 0:
			devloping.append(population)
		else:
			developed.append(population)
	developed.sort(reverse=True)
	skew = sum(developed[0:K])
	election_result.append((sum(devloping) + skew, sum(developed) - skew))
for i in election_result:
	print(i[0], i[1])

# 2
# 6 3
# 1 5
# 0 10
# 1 2
# 1 1
# 1 8
# 0 5
# 6 3
# 1 5
# 0 10
# 1 2
# 1 1
# 1 8
# 0 5