class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []        
        res = [words[0]]
        last = groups[0]
        
        for i in range(1, len(words)):
            curr = groups[i]
            if curr != last:
                res.append(words[i])
                last = curr
        return res