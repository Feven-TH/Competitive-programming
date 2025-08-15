class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dir = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def check(row,col):
            count = 0
            for dr,dc in dir:
                R = row + dr
                C = col + dc
                if 0 <= R <len(board) and 0 <= C <len(board[0]) and board[R][C] == "M":
                    count += 1
            return count 

        def dfs(r,c):
            if board[r][c] == "M":
                board[r][c] = "X"
                return 
            if board[r][c] == "E":
                count = check(r,c)
                if count == 0:
                    board[r][c] = "B"
                    for dr,dc in dir:
                        R = r + dr
                        C = c + dc
                        if 0 <= R < len(board) and 0 <= C < len(board[0]):
                            dfs(R,C)
                else:
                    board[r][c] = str(count)
        dfs(click[0],click[1])
        return board




            