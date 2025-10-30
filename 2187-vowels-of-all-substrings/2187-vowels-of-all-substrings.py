class Solution:
    def countVowels(self, word: str) -> int:
        v = {'a','e','i','o','u'}
        res = 0
        for i,ch in enumerate(word):
            if ch in v:
                res += ((i+1)*(len(word)-i))
        return res
