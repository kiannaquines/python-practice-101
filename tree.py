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
            self._insert_recurrsive(self.root, new_node)


    def _insert_recurrsive(self, current, new_node):
        if current.left is None:
            current.left= new_node
        elif current.right is None:
            current.right = new_node
        else:
            self._insert_recurrsive(current.left, new_node)

    def display(self):
        if self.root is None:
            print("Tree is empty for now")
        else:
            self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node is not None:
            self._display_recursive(node.right, level + 1)
            print(" " * level + str(node.value))
            self._display_recursive(node.left, level + 1)


if __name__ == "__main__":
    tree = Tree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)
    tree.display()