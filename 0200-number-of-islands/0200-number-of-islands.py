class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        n=len(grid)
        m=len(grid[0])
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        
        def dfs(r,c):
            if grid[r][c]=="0" :
                return
            grid[r][c]="0"
            for x,y in direction:
                new_r=x+r
                new_c=y+c
                if inbound(new_r,new_c) and  grid[new_r][new_c]!="0" :
                    dfs(new_r,new_c)
            
        islands=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    islands+=1
                    dfs(i,j)
                    
        return islands
        