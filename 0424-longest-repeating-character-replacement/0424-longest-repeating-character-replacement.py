class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = defaultdict(int)
        left, maxx, max_count = 0, 0,0
        for i in range(len(s)):
            curr[s[i]] += 1
            max_count = max(max_count,curr[s[i]] )
            while (i-left+1) - max_count >k:
                curr[s[left]] -= 1
                left += 1
            maxx = max(maxx,i- left +1)
        return maxx



