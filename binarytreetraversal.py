class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left
    

class BinaryTreeTraversal(object):
    
    # left -> root -> right
    def inorderTraversal(self, root):
        
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.value)
            inorder(node.right)
        
        inorder(root)

        return result

    # left -> right -> root
    def postorderTraversal(self, root):

        result = []

        def postorder(node):
            if node is None:
                return
            
            postorder(node.left)
            postorder(node.right)
            result.append(node.value)
        
        postorder(root)

        return result

    # root -> left -> right
    def preorderTraversal(self, root):
        result = []
        def preorder(node):
            if node is None:
                return
            
            result.append(node.value)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return result




if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(6)

    sol = BinaryTreeTraversal()
    resultInorder = sol.inorderTraversal(root)
    resultPostorder = sol.postorderTraversal(root)
    resultPreorder = sol.preorderTraversal(root)

    print(resultInorder)
    print(resultPostorder)
    print(resultPreorder)
