class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

'''
inOrder = left root right
preOrder = root left right
postOrder = left right root
levelOrder = each level
'''

def search(order, start, end, value):
	for i in range(start, end+1):
		if order[i] == value:
			return i

# We build the tree with bottom up aproach
def buildTree(inOrder, preOrder, start, end):
	# The node has reached its end
	if start > end:
		return None
	node = Node(preOrder[buildTree.index])
	buildTree.index = buildTree.index + 1

	# Terminating condition 
	if start == end:
		return node

	index = search(inOrder, start, end, node.value)
	node.left = buildTree(inOrder, preOrder, start, index-1)
	node.right = buildTree(inOrder, preOrder, index+1, end)

	# Once the node left and right subtree is done, we attach it to the parent
	return node

def printInOrder(node):
	if node is None:
		return
	printInOrder(node.left)
	print(node.value)
	printInOrder(node.right)

def printLevelOrder(node, queue=[]):
	if queue == []
		return
	for i in queue:
		print(i)
	for i in queue:
		# TODO 
		remove and enque child nodes

inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.index = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
 
# Let us test the build tree by priting Inorder traversal
print("Inorder traversal of the constructed tree is")
printInOrder(root)