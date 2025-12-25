class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        maxx = 0
        happiness.sort(reverse =True)
        for i in range(k):
            d = happiness[i] - i
            if d > 0:
                maxx += d
        return maxx
