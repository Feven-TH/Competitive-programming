class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapify(nums)
        while nums[0] < k and len(nums) >=2:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, (min(x, y) * 2 + max(x, y)))
            count += 1
        return count

