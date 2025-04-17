class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTraversal(object):
    def inOrderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)
        
        inorder(root)
        return result

    def postOrderTraversal(self, root):
        result = []

        def postorder(root):
            if root is None:
                return 
            
            postorder(root.left)
            postorder(root.right)
            result.append(root.value)
        
        postorder(root)
        return result
    
    def preOrderTraversal(self, root):
        result = []

        def preorder(root):
            if root is None:
                return 
            
            result.append(root.value)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return result

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.right = TreeNode(4)

    traversal = BinaryTraversal()
    resultInorder = traversal.inOrderTraversal(root)
    resultPostorder = traversal.preOrderTraversal(root)
    resultPreorder = traversal.postOrderTraversal(root)
    
    print("IN-ORDER", resultInorder)
    print("PRE-ORDER", resultPreorder)
    print("POST-ORDER", resultPostorder)
