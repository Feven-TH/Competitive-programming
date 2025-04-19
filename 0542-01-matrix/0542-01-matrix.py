class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = -1
                else:
                    q.append((i,j))

        directions = [(0,-1) ,(0,1), (-1,0), (1,0)]
        while q:
            i,j = q.popleft()
            for dr,dc in directions:
                row , col = i + dr , j + dc
                if inbound(row,col) and mat[row][col] == -1:
                    mat[row][col] = mat[i][j] + 1
                    q.append((row,col))
        return mat
    
       


