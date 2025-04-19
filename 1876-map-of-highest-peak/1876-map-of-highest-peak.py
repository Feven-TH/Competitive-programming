class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inbound(row, col):
            return 0 <= row < len(isWater) and 0 <= col < len(isWater[0])
        
        q = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i,j))
                else:
                    isWater[i][j] = -1
                    

        directions = [(0,-1) ,(0,1), (-1,0), (1,0)]
        while q:
            i,j = q.popleft()
            for dr,dc in directions:
                row , col = i + dr , j + dc
                if inbound(row,col) and isWater[row][col] == -1:
                    isWater[row][col] = isWater[i][j] + 1
                    q.append((row,col))
        
        return isWater