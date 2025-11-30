class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        rem = summ % p
        if rem == 0:
            return 0

        prefix = [0]*(len(nums))
        prefix[0] = nums[0]% p

        for i in range(1,len(nums)):
            prefix[i] = (prefix[i-1] + nums[i]) % p
        
        seen = {0:-1}
        minn = float('inf')
        for i in range(len(nums)):
            curr = (prefix[i] - rem) % p
            if curr in seen:
                minn = min(minn, i - seen[curr])
            seen[prefix[i]] = i
        return minn if minn < len(nums) else -1


