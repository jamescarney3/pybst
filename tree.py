class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
