class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        maps = defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maps[r-c].append(grid[r][c])
        
        for key in maps:
            if key <0:
                maps[key].sort(reverse =True)
            else:
                maps[key].sort()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = maps[r - c].pop()
        
        return grid
        