class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(root, 0, 0)])
        res = [(0, 0, root.val)]
        while queue:
            size = len(queue)
            for _ in range(size):
                node, row, col = queue.popleft()
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                    res.append((col - 1, row + 1, node.left.val))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
                    res.append((col + 1, row + 1, node.right.val))
                    
        res.sort()
        i = 0
        result = []
        while i < len(res):
            result.append([res[i][2]])
            while i + 1 < len(res) and res[i + 1][0] == res[i][0]:
                result[-1].append(res[i + 1][2])
                i += 1
            i += 1
        return result