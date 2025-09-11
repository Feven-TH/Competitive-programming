class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        v = []
        for ch in s:
            if ch.lower() in vowels:
                v.append(ch)
        v.sort()
        j = 0
        S = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                S[i] = v[j]
                j += 1
        return "".join(S)
