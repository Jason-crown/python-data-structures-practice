class Node:
    """A class representing a node in a binary search tree.
    Each node contains data and pointers to its left and right children.
    Attributes:
        data: The value stored in the node.
        left: A reference to the left child node.
        right: A reference to the right child node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)

        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

        # Ignore duplicate values

    def search(self, target):
        current = self.root

        while current is not None:
            if target == current.data:
                return True
            elif target < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current is None:
            return

        self._inorder_recursive(current.left)
        print(current.data, end=" ")
        self._inorder_recursive(current.right)

    def display(self):
        self.inorder()
        print()

# Test the tree
tree = BinarySearchTree()

for value in [8, 3, 10, 1, 6, 14]:
    tree.insert(value)

tree.display()              # 1 3 6 8 10 14

print(tree.search(6))       # True
print(tree.search(99))      # False

