class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
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
            return TreeNode(value)
        
        if value < current.value:
            current.left = self._insert(current.left, value)
        elif value > current.value:
            current.right = self._insert(current.right, value)
        
        return current
    
    def display(self):
        self._display(self.root, 0)
    
    def _display(self, current, level):
        if current is not None:
            self._display(current.right, level + 1)
            print(" " * 5 * level + str(current.value))
            self._display(current.left, level + 1)

    def _min_value_node(self, right):
        current = right

        while current and current.right is not None:
            current = current.right
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

                if current.left is None:
                    return current.right
                
                if current.right is None:
                    return current.left

                # inorder swap
                temp = self._min_value_node(current.right)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value)
        
        return current


    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, current, value):
        if current is not None:

            if current is None or current.value == value:
                return current
            
            if value < current.value:
                return self._search(current.left, value)
            elif value > current.value:
                return self._search(current.right, value)
            
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(-1)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.insert(9)
    tree.insert(7)

    tree.delete(7)
    tree.delete(9)
    tree.delete(4)
    tree.delete(3)
    tree.display()


    search = tree.search(-2)

    if search is not None:
        print(f"Node {search.value} is found in the tree")
    else:
        print(f"Node is not found in the tree")

