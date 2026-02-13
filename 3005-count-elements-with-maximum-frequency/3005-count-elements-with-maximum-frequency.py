class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxx = max(counts.values())
        return sum(maxx for c in counts if counts[c] == maxx)