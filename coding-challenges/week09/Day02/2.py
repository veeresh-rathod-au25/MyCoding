class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum=0
        def helper(root):
            if root:
                helper(root.right)
                self.sum+=root.val
                root.val=self.sum
                helper(root.left)
        helper(root)
        return root