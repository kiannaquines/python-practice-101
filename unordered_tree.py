class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class UnorderedTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
        else:
            self._recursive_insert(self.root, new_node)
            
    def _recursive_insert(self, current, new_node):
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            self._recursive_insert(current.left, new_node)
