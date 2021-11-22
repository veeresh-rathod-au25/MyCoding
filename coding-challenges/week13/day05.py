class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)
        return str(x) == reverse[::-1]
      
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[]
        ans=[]
        q.append(root)
        while q:
            s=len(q)
            z=[]
            for i in range(s):
                t=q.pop(0)
                z.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            ans.append(z)
        for i in range(1,len(ans),2):
            ans[i]=ans[i][::-1]
        return ans
