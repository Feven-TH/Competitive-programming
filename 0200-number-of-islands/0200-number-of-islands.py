class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0,1), (1,0) , (-1,0) , (0,-1)]
        island = 0

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row , col , visited):
            visited.add((row,col))
            for i,j in directions:
                Row = row + i
                Col = col + j
                if inbound(Row,Col) and grid[Row][Col] == "1" and (Row,Col) not in visited:
                    dfs(Row , Col , visited)
            return None 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row , col) not in visited :
                    island += 1
                    dfs(row , col , visited)

        return island


