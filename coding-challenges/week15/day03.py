class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for x in range(n)] for y in range(n)]
        return self.dfs(matrix, 1, 0, 0, False)
    
    def dfs(self, matrix, counter, i,j,goUp):
        if self.is_valid(i,j,matrix):      
            matrix[i][j] = counter
            if goUp:
                self.dfs(matrix, counter+1, i-1, j,True)
            self.dfs(matrix, counter+1, i, j+1,False )
            self.dfs(matrix, counter+1, i+1, j, False)
            self.dfs(matrix, counter+1, i, j-1, False)
            self.dfs(matrix, counter+1, i-1, j,  True)
        return matrix
    
    def is_valid(self, i, j, matrix):
        return not (i<0 or i > len(matrix) -1 or j<0 or j>len(matrix[0])-1 or matrix[i][j] > 0)


def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def _rec(i, j):
            if i == j:
                return [TreeNode(i)]
            if i > j:
                return [None]
            ans = []
            for k in range(i, j + 1):
                lefts = _rec(i, k - 1)
                rights = _rec(k + 1, j)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(k)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
        
        return _rec(1, n)