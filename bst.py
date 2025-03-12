class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, current, value):
        if current is None:
            return Node(value)

        if value < current.value:
            current.left = self._insert(current.left, value)
        else:
            current.right = self._insert(current.right, value)

        return current

    def display(self):
        if self.root is not None:
            self._display(self.root, 0)

    def _display(self, current, level):
        if current:
            self._display(current.right, level + 1)
            print(" " * level + str(current.value))
            self._display(current.left, level + 1)

    def search(self, value):
        return self._search(self.root, value) is not None

    def _search(self, current, value):
        if current is None or current.value == value:
            return current
        if value < current.value:
            return self._search(current.left, value)
        return self._search(current.right, value)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(8)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.display()

    result = tree.search(5)
    if result:
        print("Found")
    else:
        print("Not found")