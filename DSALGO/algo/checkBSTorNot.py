class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MAX = 999999999
INT_MIN = -INT_MAX
voilations = []
def isBST(head, min, max):
    global voilations
    if head is None:
        return True
    if head:
        if head.data < min or head.data > max:
            voilations.append(head)
            return False
        leftSubtreeResult = isBST(head.left, min, head.data-1)
        rightSubtreeResult = isBST(head.right, head.data+1, max)
        return (leftSubtreeResult and rightSubtreeResult)


'''
        10
        / \
        5  3
        /\
        2 20
        \30
''' 
# root = Node(10)
# root.right = Node(3)
# root.left = Node(5)
# root.left.left = Node(2)
# root.left.right = Node(20)
# root.left.left.right = Node(30)

# root1 = Node(8)
# root1.right = Node(10)
# root1.left = Node(2)
# root1.left.left = Node(1)
# root1.left.right = Node(6)
# root1.left.right.left = Node(4)
# root1.left.right.right = Node(7)

root2 = Node(5)
root2.left = Node(4)
root2.right = Node(8)
root2.left.left = Node(1)
root2.left.left.left = Node(0)

isBST(root2, INT_MIN, INT_MAX)
for voilation in voilations:
    print(voilation.data)



