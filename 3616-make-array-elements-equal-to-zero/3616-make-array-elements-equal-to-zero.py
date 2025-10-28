class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        count = 0
        total = sum(nums)
        prefix, suffix = 0, total

        for i in range(n):
            if nums[i] == 0:
                if 0 <= prefix - suffix <= 1:
                    count += 1
                if 0 <= suffix - prefix <= 1:
                    count += 1
            else:
                prefix += nums[i]
                suffix -= nums[i]

        return count
