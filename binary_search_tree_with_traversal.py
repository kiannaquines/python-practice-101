class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, current, value):
        if current is None:
            return TreeNode(value=value)
        
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
        return self._search(self.root, value)
    
    def _search(self, current, value):
        if current is None or current.value == value:
            return current
        
        if value < current.value:
            return self._search(current.left, value)
        elif value > current.value:
            return self._search(current.right, value)
    
    def _min_value_node(self, node):
        current = node
        
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
                
                temp = self._min_value_node(current.right)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value)
            
            return current
    
    def inorder(self):
        result = []

        def inorderTraversal(node):
            if node is None:
                return
            
            inorderTraversal(node.left)
            result.append(node.value)
            inorderTraversal(node.right)
        
        inorderTraversal(self.root)

        return result
    
    def preorder(self):
        result = []

        def preorderTraversal(node):
            if node is None:
                return
            
            result.append(node.value)
            preorderTraversal(node.left)
            preorderTraversal(node.right)
        
        preorderTraversal(self.root)

        return result
    
    def postorder(self):
        result = []

        def postorderTraversal(node):
            if node is None:
                return
            
            postorderTraversal(node.left)
            postorderTraversal(node.right)
            result.append(node.value)
        
        postorderTraversal(self.root)

        return result

            
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(0)
    tree.insert(4)
    tree.insert(6)
    tree.insert(5)
    tree.delete(4)
    tree.display()

    inorder_traversal = tree.inorder()
    print(inorder_traversal)

    preorder_traversal = tree.preorder()
    print(preorder_traversal)

    postorder_traversal = tree.postorder()
    print(postorder_traversal)
