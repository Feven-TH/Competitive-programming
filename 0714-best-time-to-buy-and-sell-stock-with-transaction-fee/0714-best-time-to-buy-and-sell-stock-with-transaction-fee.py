class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0] 
        notHold = 0 
        for i in range(1,len(prices)):
            hold = max(hold, notHold - prices[i])
            notHold = max(notHold, hold + prices[i] - fee)
        return notHold 