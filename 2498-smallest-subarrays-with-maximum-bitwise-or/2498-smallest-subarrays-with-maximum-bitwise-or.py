class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last = [0] * 32  
        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i

            max_len = 1
            for bit in range(32):
                if last[bit] >= i:
                    max_len = max(max_len, last[bit] - i + 1)

            answer[i] = max_len

        return answer