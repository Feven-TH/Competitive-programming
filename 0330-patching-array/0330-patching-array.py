class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 1
        res = 0
        i = 0
        while patch <= n:
            if i < len(nums) and patch >= nums[i]:
                patch += nums[i]
                i += 1
            else:
                patch += patch
                res += 1
        return res