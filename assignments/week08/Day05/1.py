lass Solution:
    def maxDepth(self, root):
        left = 0
        right = 0
        if root is None:
            return 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        return 1 + max(left,right)   
