class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> float:
        maxx,left= 0,0
        counts = {}
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            counts[nums[i]] = counts.get(nums[i], 0) +1
            
            if i - left +1 > k: 
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                temp -= nums[left]
                left += 1
            if i-left+ 1 == k and len(counts) == k:
                maxx = max(maxx,temp)

        return maxx
    