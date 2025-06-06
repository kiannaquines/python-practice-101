class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, current, value):
        if current is None:
            return TreeNode(value)
        
        if value == current.value:
            raise Exception('Duplicate node has been found, try new one')

        if value < current.value:
            current.left = self._insert(current.left, value)
        elif value > current.value:
            current.right = self._insert(current.right, value)

        return current

    def display(self):
        return self._display(self.root, 0)

    def _display(self, current, level):
        if current is not None:
            self._display(current.right, level+1)
            print(" " * 4 * level + str(current.value))
            self._display(current.left, level+1)
    
    def search(self, value):
        result = self._search(self.root, value)
        self.display_error_search(result)
        return result

    def display_error_search(self, search_result):
        if search_result is not None:
            print("Yhazz! Node has been found")
        else:
            print("Ohhh! Node cannot be found")

    def _search(self, current, value):
        if current is None or current.value == value:
            return current
        
        if value < current.value:
            return self._search(current.left, value)
        elif value > current.value:
            return self._search(current.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _min_value_node(self, node):
        current = node
        while current and current.right is not None:
            current = current.right
        return current

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

    def invert(self):
        return self._invert(self.root)

    def _invert(self, current):
        if current is None:
            return None

        current.left, current.right = self._invert(current.right), self._invert(current.left)        
        return current
    
    def revert(self):
        return self._revert(self.root)

    def _revert(self, current):
        if current is None:
            return None
        current.left, current.right = self._revert(current.left), self._revert(current.right)
        return current

    def preorder(self):
        return self._preorder(self.root)
    
    def _preorder(self, current):
        def traverse(node, result):
            if node is None:
                return
            result.append(node.value)
            traverse(node.left, result)
            traverse(node.right, result)
            return result

        result = []
        traverse(current, result)
        return result

    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, current):

        def traverse(node, result):
            if node is None:
                return
            
            traverse(node.left, result)
            result.append(node.value)
            traverse(node.right, result)

            return result

        result = []
        traverse(current, result)        
        return result

    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self, current):

        def traverse(node, result):
            if node is None:
                return

            traverse(node.left, result)
            traverse(node.right, result)
            result.append(node.value)

            return result

        result = []
        traverse(current, result)
        return result

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(6)
    tree.display()

    preorder = tree.preorder()
    inorder = tree.inorder()
    postorder = tree.postorder()

    print(f'Preorder: {preorder}')
    print(f'Inorder: {inorder}')
    print(f'Postorder: {postorder}')
