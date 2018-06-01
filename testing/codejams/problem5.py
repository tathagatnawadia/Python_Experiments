T = int(input())
test_counter = 1
while test_counter <= T:
	test_counter = test_counter + 1
	no_of_nodes = int(input())
	linked_list = list(map(int, input().split()))
	pivot = int(input())
	_a = linked_list.index(pivot)
	_b = linked_list[_a:0]
	_c = linked_list[_a:]
	print(_b)
	print(_c)

# 1
# 8
# 1 2 2 4 5 6 7 8
# 4