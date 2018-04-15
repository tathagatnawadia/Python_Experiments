'''
Input : 4 -> 4 -> 0 -> 2 -> 3 -> 4 -> 
        3 -> 3 -> 0 -> 4 -> 
Output : 8-> 2-> 3-> 4-> 6-> 4-> 0-> 
         0-> 0-> 0-> 

Explanation :
First, after doubling the first element and making
second element 0 before all zeros.
8 -> 0 -> 0 -> 2 -> 3 -> 4 -> 6 -> 0 
-> 0 -> 4 ->
Next :
8 -> 6 -> 5 -> 6 -> 0 -> 0 -> 0 -> 
0 -> 0 -> 0 -> 0 -> 

Input : 0 -> 4 -> 4 -> 0 -> 3 -> 3 -> 0 
        -> 5 -> 0 -> 0 -> 6 ->
Output : 8 -> 6 -> 5 -> 6 -> 0 -> 0 -> 0 
         -> 0 -> 0 -> 0 -> 0 ->
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def double_duplicates(root):
	while root is not None:
		if root.data == 0:
			root = root.next
			continue
		if root.next is not None:
			if root.data == root.next.data:
				root.data *= 2
				root.next.data = 0
				root = root.next.next
			else:
				root = root.next
		else:
			root = root.next

def mergeZeroes(root):
	prev = None
	count = 0

def printList(root):
	while root is not None:
		print(root.data, '->', end='')
		root = root.next

head = Node(4)
head.next = Node(4);
head.next.next = Node(0);
head.next.next.next = Node(2);
head.next.next.next.next = Node(3);
head.next.next.next.next.next = Node(4);
head.next.next.next.next.next.next = Node(3);
head.next.next.next.next.next.next.next = Node(3);
head.next.next.next.next.next.next.next.next = Node(0);
head.next.next.next.next.next.next.next.next.next = Node(4);

printList(head)
double_duplicates(head)
print()
printList(head)