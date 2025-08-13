class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def coordinates(square):
            row = n -1 - (square -1)//n
            col = (square-1) %n
            if (n-1-row) %2 != 0:
                col = n -1 -col
            return row,col
        
        seen = set()
        q = deque([(1,0)])
        while q:
            curr,moves = q.popleft()
            if curr == n**2:
                return moves
            for i in range(1,7):
                nxt = curr + i
                if nxt > n**2:
                    continue

                r,c = coordinates(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in seen:
                    q.append((nxt, moves+1))
                    seen.add(nxt)
        return -1




