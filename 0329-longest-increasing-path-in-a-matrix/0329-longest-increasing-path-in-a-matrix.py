class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        def inBounds(i,j):
            return 0 <= i < rows and 0 <= j < cols
    
        def dfs(i,j):
            if memo[i][j] != -1:
                return memo[i][j]
            maxx = 1
            for dr,dc in directions:
                x,y = i+ dr , j+ dc
                if inBounds(x,y) and matrix[i][j] < matrix[x][y]:
                    length = 1 + dfs(x,y)
                    maxx = max(maxx, length)
            memo[i][j] = maxx
            return maxx
        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(res, dfs(row, col)) 
        return res



                