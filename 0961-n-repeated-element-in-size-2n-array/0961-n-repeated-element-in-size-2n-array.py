class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key,val in count.items():
            if val == len(nums)//2:
                return key
    