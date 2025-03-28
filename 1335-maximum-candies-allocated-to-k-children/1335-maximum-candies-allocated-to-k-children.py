class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def validate(mid):
            count = 0
            for c in candies:
                count += (c//mid)
            return count >= k

        if sum(candies) < k: 
            return 0
        low , high = 1 , max(candies)
        res = low
        while low <= high:
            mid = (low + high) //2
            if validate(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res