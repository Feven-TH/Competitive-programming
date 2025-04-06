class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        nums = [instructions[0]]
        for i in range(1 , len(instructions)):
            left = bisect_left(nums , instructions[i])
            right = bisect_right(nums , instructions[i])
            cost += min(left , len(nums) - right)
            nums.insert(left , instructions[i])
        return cost % (10**9 + 7)
