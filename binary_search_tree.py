class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, current, value):
        if current is None:
            return Node(value)

        if value < current.value:
            current.left = self._insert(current.left, value)
        elif value > current.value:
            current.right = self._insert(current.right, value)

        return current

    def display(self):
        if self.root is None:
            print("Tree is empty at the moment")
        else:
            self._display(self.root, 0)

    def _display(self, current, level):
        if current:
            self._display(current.right, level + 1)
            print(" " * level + str(current.value))
            self._display(current.left, level + 1)

if __name__ == "__main__":
    tree = Tree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(8)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.display()
