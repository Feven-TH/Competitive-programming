class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            g = 0
            for j in range(i,len(nums)):
                if g == 0:
                    g = nums[j]
                else:
                    g = gcd(g,nums[j])
                if g == k:
                    res += 1
        return res