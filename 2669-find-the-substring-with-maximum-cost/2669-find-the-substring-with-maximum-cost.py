class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        maps = {key: (vals[chars.index(key)] if key in chars else ord(key) - ord('a') + 1) for key in s}
        curr, maxx = 0, float('-inf')
        for char in s:
            curr = max(curr + maps[char], maps[char])
            maxx = max(maxx,curr)
        return maxx if maxx > 0 else 0     