class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        for ch in s:
            if ch in {'a','e','i','o','u'}:
                count += 1
        if count ==0:
            return False
        else:
            return True


