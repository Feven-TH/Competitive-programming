class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        seen = {0: -1}
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        max_len = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= vowels[c]
            
            if mask not in seen:
                seen[mask] = i
            else:
                max_len = max(max_len, i - seen[mask])
        
        return max_len