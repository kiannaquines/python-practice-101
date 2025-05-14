class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, current, value):
        if current is None:
            return TreeNode(value)
        
        if value == current.value:
            pass

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
    
    def invertTree(self):
        return self._invertTree(self.root)
    
    def _invertTree(self, current):
        if current is None:
            return None
        
        current.left, current.right = self._invertTree(current.right), self._invertTree(current.left) 
        return current

    def reverseTree(self):
        return self._reverseTree(self.root)
    
    def _reverseTree(self, current):
        if current is None:
            return None
        
        current.left, current.right = self._reverseTree(current.left), self._reverseTree(current.right)
        return current
    
    def preorder(self):
        return self._preorder(self.root)
    
    def _preorder(self, current):
        result = []
        def preOrderTraversal(node):
            if node is None:
                return
            
            result.append(node.value)
            preOrderTraversal(node.left)
            preOrderTraversal(node.right)
        
        preOrderTraversal(current)
        return result

    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, current):
        result = []
        def inorderTraversal(node):
            if node is None:
                return
            inorderTraversal(node.left)
            result.append(node.value)
            inorderTraversal(node.right)
        
        inorderTraversal(current)

        return result
    
    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self, current):
        result = []
        def postorderTraversal(node):
            if node is None:
                return
            
            postorderTraversal(node.left)
            postorderTraversal(node.right)
            result.append(node.value)

        postorderTraversal(current)
        return result

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.delete(6)
    tree.delete(4)
    tree.delete(5)
    tree.display()

    if tree.search(10) is not None:
        print('\nNode found')
    else:
        print('\nNode cannot be found')

    print("\nInverse Tree")
    tree.invertTree()
    tree.display()

    print("Reverse Tree")
    tree.reverseTree()
    tree.display()

    print("\n\nTree Traversal\n\n")
    preorderTraversal = tree.preorder()
    print(f"Pre-Order Traversal: {preorderTraversal}")
    inorderTraversal = tree.inorder()
    print(f"In-Order Traversal: {inorderTraversal}")
    postorderTraversal = tree.postorder()
    print(f"Post-Order Traversal: {postorderTraversal}")
