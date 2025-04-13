class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(row):
            visited.add(row)
            
            for i in range(len(isConnected)):
                if isConnected[row][i] == 1 and i not in visited:
                    dfs(i)
            
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        
        return provinces


            
