class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c = 1
        res = 0
        for i in range(1,len(prices)):
            if prices[i - 1] - prices[i] == 1:
                c += 1
            else:
                t = c*(c+1)//2
                res += t
                c = 1
        res += c*(c+1)//2 
        return res

