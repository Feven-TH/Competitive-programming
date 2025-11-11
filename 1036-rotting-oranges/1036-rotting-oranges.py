class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        
        
        directions = [(0 , 1) , (0, -1) , (1 , 0) , (-1 , 0)]
        
        def inbound(r , c):
            return 0 <= r < row and 0 <= c < col
        
        fresh = 0
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r , c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        if fresh == 0:
            return 0
        
        time = 0
        while queue:
            
            for i in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr = r + dr
                    nc = c + dc      
                    if inbound(nr , nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr , nc))
            time += 1
            

        if fresh:
            return -1   
        return time - 1
                        
                        
        

        
        
        
        
        
        
        
