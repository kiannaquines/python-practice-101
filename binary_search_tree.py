class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearch:
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
        return self._display(self.root, 0)
    
    def _display(self, current, level):
        if current is not None:
            self._display(current.right, level + 1)
            print(" " * 4 * level + str(current.value))
            self._display(current.left, level + 1)
            
            
    def search(self, search_value):
        return self._search(self.root, search_value)
    
    def _search(self, current, search_value):
        if current is None or current.value == search_value:
            return current
        
        if search_value < current.value:
            return self._search(current.left, search_value)
        elif search_value > current.value:
            return self._search(current.right, search_value)
        
        return current
    
    def _min_node_value(self, value):
        current = value
        
        while current and current.left is not None:
            current = current.left
        
        return current
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, current, value):
        if current is not None:
            
            if value < current.value:
                current.left = self._delete(current.left, value)
            elif value > current.value:
                current.right = self._delete(current.right, value)
            else:
                # case 1
                if current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                
                # case 2
                temp = self._min_node_value(current.right)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value)
            
            return current                
            
        
    
tree = BinarySearch()
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

tree.display()

search_node = 10


if tree.search(search_node) is not None:
    print(f"Node {search_node} is found")
else:
    print(f"Node {search_node} cannot be found")

delete_node = 7    
    
if tree.delete(delete_node):
    print(f"Node {delete_node} has been deleted")
else:
    print(f"Node {delete_node} cannot be deleted")

tree.display()
