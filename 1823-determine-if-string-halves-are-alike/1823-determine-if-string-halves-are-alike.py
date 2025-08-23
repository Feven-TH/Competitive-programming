class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s)//2
        a,b = s[:mid],s[mid:]
        countA = sum(1 for ch in a if ch in vowels)
        countB = sum(1 for ch in b if ch in vowels)

        return countA == countB
