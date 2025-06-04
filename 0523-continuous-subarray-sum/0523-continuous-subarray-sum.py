class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        maps = {0:-1}
        prefix = [0] * len(nums)
        prefix[0] = nums[0]  
        
        for i in range(1,len(nums)):
            prefix[i] = prefix [i - 1] + nums[i] 

        for i in range(len(prefix)):
            prefix[i] = prefix[i] % k
        # print(prefix)
        for i in range(len(prefix)):
            if prefix[i] in maps:
                if i - maps[prefix[i]] >= 2:
                    return True
            else:
                maps[prefix[i]] = i 
        return False
        
        
            
