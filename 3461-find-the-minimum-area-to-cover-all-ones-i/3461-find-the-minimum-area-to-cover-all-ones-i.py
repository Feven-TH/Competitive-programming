class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, top, bottom = float('inf'), -float('inf'), float('inf'), -float('inf')
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    left, right = min(left,i), max(right,i)
                    top, bottom = min(top,j), max(bottom,j)
        return (right-left+1)*(bottom-top+1)
