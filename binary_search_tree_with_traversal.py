class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.result = []
    
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
            print(" " * 4 * level + str(current.value))
            self._display(current.left, level + 1)
    
    def search(self, value):
        result = self._search(self.root, value)

        if result is not None:
            print(f'Node {result.value} found in the tree.')
        else:
            print('Node cannot be found, please try again.')
    
    def _search(self, current, value):
        if current is None or current.value == value:
            return current
        
        if value < current.value:
            return self._search(current.left, value)
        elif value > current.value:
            return self._search(current.right, value)
    
    def _min_value_node(self, right):
        current = right
        
        while current and current.right is not None:
            current = current.right
        
        return current

    def delete(self, node):
        self.root = self._delete(self.root, node)
    
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

                
                temp = self._min_value_node(current.right)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value)
        
        return current
    
    def inorder(self):
        result = self.result.copy()
        def inorder_traversal(node):
            if node is None:
                return 
            
            inorder_traversal(node.left)
            result.append(node.value)
            inorder_traversal(node.right)
        
        inorder_traversal(self.root)
        return result
    
    def postorder(self):
        result = self.result.copy()
        def postorder_traversal(node):
            if node is None:
                return 
            
            postorder_traversal(node.left)
            postorder_traversal(node.right)
            result.append(node.value)

        
        postorder_traversal(self.root)
        return result
    
    def preorder(self):
        result = self.result.copy()

        def preorder_traversal(node):
            if node is None:
                return 
            result.append(node.value)
            preorder_traversal(node.left)
            preorder_traversal(node.right)
        
        preorder_traversal(self.root)
        return result


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.delete(7)

    tree.display()

    preorder = tree.preorder()
    print(f'Pre-order: {preorder}')

    inorder = tree.inorder()
    print(f'In-order: {inorder}')

    postorder = tree.postorder()
    print(f'Post-order: {postorder}')

