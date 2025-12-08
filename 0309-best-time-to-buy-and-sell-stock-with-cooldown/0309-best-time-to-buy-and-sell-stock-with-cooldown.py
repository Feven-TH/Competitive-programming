class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0
        for i in range(1,len(prices)):
            p = prices[i]
            h,s,r = hold, sold, rest
            hold = max(h, rest - p)
            sold = h + p
            rest = max(r, s)
        return max(rest, sold)