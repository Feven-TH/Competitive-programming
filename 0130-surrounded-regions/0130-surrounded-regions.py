class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        directions = [(0,1), (1,0) , (-1,0) , (0,-1)]
        
        
        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))

                
        def dfs(i,j):
            board[i][j] = -1
            for dr, dc in directions:
                R ,C = i +dr , j + dc
                if inbound(R,C) and board[R][C] == "O":
                    dfs(R,C)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == r-1 or j == c-1):
                    dfs(i,j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == -1:
                    board[i][j] = "O"

