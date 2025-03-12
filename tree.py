class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        elif new_node.value > current.value:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def display_preorder(self):
        if self.root is None:
            print("Tree is currently empty")
        else:
            print("Pre-order:", end=" ")
            self._preorder(self.root)
            print()

    def _preorder(self, node):
        if node is not None:
            print(node.value, end=" ")  # Visit root first
            self._preorder(node.left)  # Then left
            self._preorder(node.right) # Then right

    def display_inorder(self):
        if self.root is None:
            print("Tree is currently empty")
        else:
            print("In-order:", end=" ")
            self._inorder(self.root)
            print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)   # Left first
            print(node.value, end=" ") # Then root
            self._inorder(node.right)  # Then right

    def display_postorder(self):
        if self.root is None:
            print("Tree is currently empty")
        else:
            print("Post-order:", end=" ")
            self._postorder(self.root)
            print()

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)  # Left first
            self._postorder(node.right) # Then right
            print(node.value, end=" ")  # Then root

    def search(self, value):
        return self._search(self.root, value) is not None

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

if __name__ == "__main__":
    tree = Tree()
    for val in [1, 2, 3, 4, 5, 6, 7, 8]:
        tree.insert(val)
    tree.display_preorder()  # Pre-order traversal
    tree.display_inorder()   # In-order traversal (original display)
    tree.display_postorder() # Post-order traversal