class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles == 0:
                moves += target - 1
                return moves
            if target%2 == 0 and maxDoubles > 0:
                target = target // 2
                moves += 1
                maxDoubles -= 1
            else:
                target -= 1
                moves += 1
        return moves
