class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        
        while root or stack:
            result.append(root.val)
            for node in root.children[::-1]:
                stack.append(node)
            root = stack.pop() if stack else None
            
        
        return result