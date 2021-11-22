class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(r):
            h = 0
            while r:
                r = r.left
                h += 1
            return h
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        hl = getHeight(root.left)
        hr = getHeight(root.right)
        if hl == hr:
            return int(2**hl) + self.countNodes(root.right)
        elif hl > hr:
            return int(2**hr) + self.countNodes(root.left)
