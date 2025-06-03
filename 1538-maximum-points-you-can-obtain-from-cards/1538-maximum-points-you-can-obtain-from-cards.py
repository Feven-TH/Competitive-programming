class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, minn, summ = 0, float('inf'), 0
        n = len(cardPoints)
        for i in range(n):
            summ += cardPoints [i]
            while i - left + 1 >n-k:
                summ -= cardPoints[left] 
                left +=1
            if i - left + 1 == n - k:  
                minn = min(minn, summ)
        return sum(cardPoints) - minn
