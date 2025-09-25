class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = defaultdict(bool)
        def dp(i):
            if i >= len(s):
                return True
            if i not in memo:
                flag = False
                for word in wordDict:
                    if s.startswith(word,i):
                        if dp(i + len(word)):
                            flag = True
                            return True
                memo[i] = flag
            return memo[i]
        return dp(0)