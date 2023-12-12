# Creating a BST library, which has the function next_smallest that prints the next smallest leaf in the tree. 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

class Iterator:
    def __init__(self, bst):
        self.bst = bst
        self.stack = []
        self.iterate(self.bst)
        self.stack.sort(reverse=True)

    def iterate(self, bst):
        if bst is not None:
            self.iterate(bst.left)
            self.stack.append(bst.val)
            self.iterate(bst.right)
        

    def next_smallest(self):
        return self.stack.pop()

    def has_next(self):
        return len(self.stack) > 0

def test1():       
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    root.left.right = Node(22)
    root.right = Node(35)
    root.right.left = Node(32)
    root.right.right = Node(40)
    
    it = Iterator(root)
    print("size", len(it.stack))
    while it.has_next():
        print(it.next_smallest())

test1()
