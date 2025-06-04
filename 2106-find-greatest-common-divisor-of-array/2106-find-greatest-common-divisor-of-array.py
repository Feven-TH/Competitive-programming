class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        x,y = nums[0] ,nums[-1]
        maxx = 1
        for i in range(2,x+1):
            if x % i == 0 and y%i == 0:
                maxx = max(maxx,i)
        return maxx


