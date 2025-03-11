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
            self._insert_recurrsive(self.root, new_node)
    
    def _insert_recurrsive(self, current, new_node):
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            self._insert_recurrsive(current.left, new_node)
    
    def display(self):
        if self.root is None:
            print("The tree is empty")
        else:
            self._display_nodes(self.root, 0)
            
    def _display_nodes(self, node, level):
        if node is not None:
            self._display_nodes(node.right, level + 1)
            print(" " * level + str(node.value))
            self._display_nodes(node.left, level + 1)
            
if __name__ == "__main__":
    tree = UnorderedTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.display()
            
