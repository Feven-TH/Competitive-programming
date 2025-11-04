class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        i,j = 0, len(height) -1
        while i <j:
            curr = min(height[i], height[j])* (j-i)
            maxx = max(maxx,curr)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxx
