class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = [0]* 10
        bitmask = []
        bit = 0
        for char in word:
            ind = ord(char) - ord("a")
            freq[ind] += 1
            bit = 0
            for i in range(10):
                if freq[i] %2 == 1:
                    bit |= (1 << i)    
            bitmask.append(bit)

        counts = {0: 1}
        res = 0
        for state in bitmask:
            res += counts.get(state,0)
            for i in range(10):
                flip = state ^ (1<<i)
                res += counts.get(flip,0)
            counts[state] = counts.get(state,0) + 1
        return res

        
        
