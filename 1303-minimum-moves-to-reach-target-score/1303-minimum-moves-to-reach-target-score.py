class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and  maxDoubles > 0 :
            if target % 2 == 0:
                res +=1
                maxDoubles -= 1
                target //= 2
            else:
                res +=1
                target -= 1
        res += (target -1)
        return res

