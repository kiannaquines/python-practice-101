class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, current, value):
        if current is None:
            return Node(value)
        
        if value == current.value:
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
    
    def _min_value_node(self, value):
        current = value
        while current.left is not None:
            current = current.left
        
        return current
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            
            if node.left is None or node.right is None:
                return None
            
            if node.left is not None:
                return node.right
                
            if node.right is not None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
            
        return node



if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    tree.insert(9)
    tree.insert(21)
    tree.insert(20)
    tree.insert(30)
    tree.insert(41)
    tree.insert(10)
    tree.display()
    
    
    search_node = 99
    
    result = tree.search(search_node)
    
    if result:
        print(f"Node {search_node} found")
    else:
        print(f"Node {search_node} cannot be found")
        
        
    delete_node = 41
    result_delete = tree.delete(delete_node)

    tree.display()
        
