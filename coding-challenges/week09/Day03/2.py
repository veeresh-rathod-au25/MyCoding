class Solution:
    def __init__(self):
        self.res = 0
    
    def traversal(self, node, cur_number):
        if node == None:
            return None
        
        cur_number = (cur_number << 1) | node.val
        
        if not node.left and not node.right:
            self.res += cur_number
            return None
        
        self.traversal(node.left, cur_number)
        
        self.traversal(node.right, cur_number)
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, 0)
        
        return self.res