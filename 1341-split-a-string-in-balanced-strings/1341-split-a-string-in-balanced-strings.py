class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L , R = 0 , 0
        counts = 0
        for c in s:
            if L == R:
                L = 0
                R = 0
                counts += 1
            if c == 'L':
                L += 1
            else:
                R += 1
        return counts
