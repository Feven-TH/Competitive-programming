class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        def win(nums , curr):
            if len(nums) == 1:
                return nums[0]

            index = (curr + k - 1 ) % len(nums)
            nums.pop(index)
            return win(nums, index)
            
        return win(nums,0)
        