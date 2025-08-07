class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        Sorted = sorted(freq.values(), reverse = True)
        keys = 8
        res = 0

        for i,f in enumerate(Sorted):
            press = (i//keys) +1
            res += f*press
        
        return res