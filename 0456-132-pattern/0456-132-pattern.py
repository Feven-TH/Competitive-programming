class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack  = []
        minn = nums[0]

        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0] > num and num > stack[-1][1]:
                return True
            stack.append([num, minn])
            minn = min(minn , num)
        return False

      