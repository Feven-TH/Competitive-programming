class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ans = [-1]*n
        cols = [False] * n   
        d1 = [False]*(2 * n - 1)
        d2 = [False]*(2 * n - 1)
        def makeBoard():
            board = []
            for r in range(n):
                temp = ["."]*n
                temp[ans[r]] = "Q"
                board.append("".join(temp))
            return board

        def backtrack(row):
            if row == n:
                res.append(makeBoard())
                return
            
            for col in range(n):
                D1 = row - col + (n-1)
                D2 = row + col
                if cols[col] or d1[D1] or d2[D2]:
                    continue
                
                ans[row] = col
                cols[col] = True
                d1[D1] = True
                d2[D2] = True

                backtrack(row+1)
                ans[row] -= 1
                cols[col] = False
                d1[D1] = False
                d2[D2] = False

        backtrack(0)
        return res
