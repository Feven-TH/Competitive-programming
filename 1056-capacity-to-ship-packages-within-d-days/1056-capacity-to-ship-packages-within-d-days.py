class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(mid, days):
            count = 1
            summ = 0
            for w in weights:
                if summ + w > mid:
                    count += 1
                    summ = w
                else:
                    summ += w
            if count <= days:
                return True
            else:
                False

        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = (low + high)//2
            if validate(mid , days) :
                high = mid - 1                
            else:
                low = mid + 1
        # if low < n and isBadVersion(low):
        return low