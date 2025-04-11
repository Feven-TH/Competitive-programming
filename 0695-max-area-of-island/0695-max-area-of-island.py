class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxx = max(maxx, dfs(i, j))

        return maxx
