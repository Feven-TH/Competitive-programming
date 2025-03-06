class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minn = deque()
        maxx = deque()
        longest = 0
        left = 0

        for i in range(len(nums)):
            while minn and nums[minn[-1]] > nums[i]:
                minn.pop()
            minn.append(i)

            while maxx and nums[maxx[-1]] < nums[i]:
                maxx.pop()
            maxx.append(i)

            while nums[maxx[0]] - nums[minn[0]] > limit:
                left += 1
                if maxx[0] < left:
                    maxx.popleft()
                if minn[0] < left:
                    minn.popleft()
            longest = max(longest , i - left + 1)
        return longest
