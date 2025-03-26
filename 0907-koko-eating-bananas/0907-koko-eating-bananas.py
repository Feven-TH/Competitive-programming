class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(mid):
            count = 0
            for p in piles:        
                count += math.ceil(p/mid)
    
            return count <= h
        
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            if canEat(mid) :
                high = mid - 1                
            else:
                low = mid + 1
        return low