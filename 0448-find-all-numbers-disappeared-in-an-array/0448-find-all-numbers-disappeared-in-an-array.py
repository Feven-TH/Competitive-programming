class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i +1 and nums[i] != nums[nums[i] - 1]:
                pos = nums[i] - 1
                nums[i] , nums[pos] = nums[pos] , nums[i]
            else:
                i += 1
        # print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


