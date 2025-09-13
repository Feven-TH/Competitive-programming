class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = defaultdict(int)
        consonants = defaultdict(int)
        for c in s:
            if c in {'a','e','i','o','u'}:
                vowels[c] += 1
            else:
                consonants[c] += 1
        return max(vowels.values(),default=0)+ max(consonants.values(),default=0)