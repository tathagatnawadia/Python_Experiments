class Node: #BST
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def iter_in_order(self):
        if self.left:
            yield from self.left.iter_in_order()
        yield self.value
        if self.right:
            yield from self.right.iter_in_order()


def decode(arg_script):
    root = Node(1)

    fresh_idx = 2
    I_node = root
    D_node = root

    for char in arg_script:
        if fresh_idx > 9:
            return -1 #invalid input, would force me to use digits > 9
        
        new_node = Node(fresh_idx)
        if char == "N":
            I_node.right = new_node
            I_node = new_node
            D_node = new_node
        elif char == "M":
            D_node.left = new_node
            D_node = new_node

        fresh_idx += 1


    return "".join([str(idx) for idx in root.iter_in_order()])


print(decode("NMM"))
