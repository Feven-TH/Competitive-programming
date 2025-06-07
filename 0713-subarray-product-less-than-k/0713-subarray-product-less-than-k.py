class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count, temp , left = 0 ,1 ,0
        for i in range(len(nums)):
            temp *= nums[i]
            while temp >= k and left<=i:
                temp //= nums[left]
                left += 1
            count += i -left +1
        return count