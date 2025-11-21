class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left,right = {}, {}
        for i,ch in enumerate(s):
            if ch not in left:
                left[ch] = i
            right[ch] = i
        
        res = 0
        for ch in left:
            l,r = left[ch], right[ch]
            if r - l > 1:
                b = len(set(s[l+1:r]))
                res += b
        return res


