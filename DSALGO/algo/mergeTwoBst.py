class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


'''
        10
        / \
        5  3
        /\
        2 20
        \30
''' 

output = []

def stackTrace(stack):
	for i in stack:
		print(i.data, end=" ")
	print()

def pushLeftMost(center):
	gen = []
	while center != None:
		gen.append(center)
		center = center.left
	return gen

def populate(center):
	gen = []
	gen = pushLeftMost(center)
	if len(gen) == 0:
		gen = pushLeftMost(center.right)
	return gen

def merge(root1, root2):
	stack1 = populate(root1)
	stack2 = populate(root2)
	stackTrace(stack1)
	stackTrace(stack2)

	while len(stack1) != 0 and len(stack2) != 0:
		a = stack1[-1]
		b = stack2[-1]

		candidate = None

		if a.data < b.data:
			candidate = stack1.pop()
			if candidate.right != None:
				stack1.extend(populate(candidate.right))
		else:
			candidate = stack2.pop()
			if candidate.right != None:
				stack2.extend(populate(candidate.right))

		output.append(candidate)

	stackTrace(output)
	stackTrace(stack1)
	stackTrace(stack2)



root1 = Node(8)
root1.right = Node(10)
root1.left = Node(2)
root1.left.left = Node(1)
root1.left.right = Node(6)
root1.left.right.left = Node(4)
root1.left.right.right = Node(7)

root2 = Node(5)
root2.left = Node(4)
root2.right = Node(8)
root2.left.left = Node(1)
root2.left.left.left = Node(0)
root2.right.left = Node(6)
root2.right.right = Node(11)

merge(root1, root2)


