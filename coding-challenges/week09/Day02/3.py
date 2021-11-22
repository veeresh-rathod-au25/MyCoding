class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stack=[]
        cur=root
        while cur is not None or stack is not None:
            while cur is not None:
                stack.append(cur)
                cur=cur.left
            
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right