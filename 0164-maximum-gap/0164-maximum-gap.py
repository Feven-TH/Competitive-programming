class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        minn,maxx = min(nums), max(nums)
        n = len(nums)
        if minn == maxx:
            return 0

        size = max(1,(maxx - minn) //(n - 1))
        count = (maxx - minn) //size + 1
        buckets = [None]*count

        for num in nums:
            idx = (num - minn) //size
            if buckets[idx] is None:
                buckets[idx] = [num, num]
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = None
        for b in buckets:
            if b is None:
                continue
            if prev_max is not None:
                max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]

        return max_gap