class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # Instead of left/right, use a list

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, parent_value, child_value):
        if self.root is None:
            self.root = Node(parent_value)
            self.root.add_child(Node(child_value))
        else:
            parent_node = self._find(self.root, parent_value)
            if parent_node:
                parent_node.add_child(Node(child_value))

    def _find(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found = self._find(child, value)
            if found:
                return found
        return None

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            print("  " * level + str(node.value))
            for child in node.children:
                self.display(child, level + 1)


if __name__ == "__main__":
    tree = Tree(1)  # Root node
    tree.insert(1, 2)
    tree.insert(1, 3)
    tree.insert(1, 1)
    tree.insert(2, 4)
    tree.insert(2, 5)
    tree.insert(3, 6)
    tree.insert(3, 7)
    tree.display()