class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = []
        for word in words:
            temp = 0
            for ch in word:
                ind = ord(ch) - ord("a")
                temp |= (1<<ind)
            bitmask.append(temp)
        # print(type(bitmask[0]))
        res = 0
        for i in range(len(words)):
            for j in range(len(words)):
                temp = bitmask[i] & bitmask[j]
                if temp.bit_count() == 0:
                    res = max(res, len(words[i])* len(words[j])) 
        return res

