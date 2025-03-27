class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(k):
            prefix = [0] * (len(nums) + 1)
            for i in range(k):
                ind = queries[i]
                prefix[ind[0]] += ind[2]
                prefix[ind[1] + 1] -= ind[2]
                
            for i in range(1,len(prefix)):  
                prefix[i] += prefix[i - 1] 
                
            for i in range(len(nums)):
                if nums[i] - prefix[i] > 0:
                    return False
            return True
            

        flag = False
        low , high = 0 , len(queries)
        res = high 

        while low <= high:
            mid = (low + high)//2
            print(validate(mid))
            if validate(mid):
                flag = True
                res = mid
                high = mid - 1                
            else:
                low = mid + 1
        
        if flag:
            return res
        else:
            return -1


