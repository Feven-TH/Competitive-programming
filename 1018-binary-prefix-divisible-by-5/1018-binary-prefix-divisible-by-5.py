class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x,res = 0,[]
        for num in nums:
            x = (2*x) + num
            if x % 5:
                res.append(False)
            else:
                res.append(True)                
        return res