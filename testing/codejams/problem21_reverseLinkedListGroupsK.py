'''
Reverse Linked list in groups of k
1->2->3->4->5->6->7->8->Null
3->2->1->6->5->4->8->7->Null
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    while head:
        print(head.data,"->",end="")
        head = head.next
    print()

newhead = None
def reverse(curr, prev):
    global newhead 
    # If last node mark it head
    if curr.next is None :
        # store the new head in a global variable
        newhead = curr
        # Make the new head point back to the previous one
        curr.next = prev
        return
    # Get the next 2 from 1.next
    next = curr.next
    # 1.next = previous (in first case its null) 2.next = 1 
    curr.next = prev
    # Tail recursion
    reverse(next, curr)

def reverse_ingroup(root, k):
    last = None
    glolbalhead = None
    firstIter = True
    while root:
        counter = 1
        head = root
        while counter < k and root.next is not None:
            root = root.next
            counter += 1
        tail = root
        root = root.next
        tail.next = None
        reverse(head, None)
        if firstIter:
            glolbalhead = newhead
            print(glolbalhead.data)
            firstIter = False
            last = newhead
            while last.next is not None:
                last = last.next
        else:
            print(last.data)
            last.next = newhead
            last = newhead
            while last.next is not None:
                last = last.next
    return glolbalhead
        



root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)

printList(root)
#reverse(root, None)
#printList(newhead)
glolbalhead = reverse_ingroup(root, 3)
printList(glolbalhead)