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
            
        if current.value == value:
            pass
        
        if value < current.value:
            current.left = self._insert(current.left, value)
        elif value > current.value:
            current.right = self._insert(current.right, value)
        
        return current
    
    def display(self):
        if self.root is not None:
            self._display(self.root, 0)
    
    def _display(self, current, level):
        if current:
            self._display(current.right, level + 1)
            print(" " * 4 * level + str(current.value))
            self._display(current.left, level + 1)
            
    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
    
    def _search(self, current, value):
        
        if current is None or current.value == value:
            return current
        
        if value < current.value:
            return self._search(current.left, value)
        elif value > current.value:
            return self._search(current.right, value)
        
        return current
        
    def _min_value_node(self, node):
        current = node
        while current and current.left is not None:
            current = current.left
        return current
        
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:            
            # Case 1: Node has only one child
            if current.left is None:
                return current.right  # Return the right child
            elif current.right is None:
                return current.left  # Return the left child

            # Case 2: Node has two children
            temp = self._min_value_node(current.right)  # Find the inorder successor
            current.value = temp.value  # Replace value with inorder successor
            current.right = self._delete(current.right, temp.value)  # Delete the inorder successor

        return current
    
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(4)
    tree.insert(1)
    tree.insert(0)
    tree.insert(5)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)
    tree.display()
    
    result = tree.search(4)
    if result:
        print(f"Found {result.value} in the tree")
    else:
        print("Cannot be found")
    
    node_to_delete = 6
    tree.delete(node_to_delete)
    tree.display()
