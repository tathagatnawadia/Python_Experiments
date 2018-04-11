

from operator import itemgetter

def sort_tasks(tasks):
	return sorted(tasks, key=lambda task:task[1])

def sort_tasks_ig(tasks):
	# Instead of using lambda function which is an overhead
	# using builtin c++ implementation of getting the sort value
	# (Task1, Prio1) -> itemgetter(1) -> Prio1 (sorting key)
	return sorted(tasks, key=itemgetter(1))

if __name__ == '__main__':
	import random 
	random.seed(100)

	tasks = [(f'task{i}', i) for i in range(1000)]
	random.shuffle(tasks)