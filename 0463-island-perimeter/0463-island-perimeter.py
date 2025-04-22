class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        directions = [(0,1), (1,0) , (-1,0) , (0,-1)]
        perimeter = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0 :
                return 1
            if (r,c)  in seen: 
                return 0
                
            seen.add((r,c))
            
            perimeter = 0
            for dr, dc in directions:
                R = dr + r
                C = dc + c
                perimeter += dfs(R,C)
        
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)

        return 0