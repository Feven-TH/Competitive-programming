class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(maxx):
            count,summ = 1,0
            for num in nums:
                if summ+num >maxx:
                    count += 1
                    summ = num
                else:
                    summ += num
            return count <= k

        low,high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if valid(mid):
                high = mid
            else:
                low = mid + 1
        return low