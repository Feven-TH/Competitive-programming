class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return
            backtrack(i + 1, path + s[i])
            if s[i].isalpha():
                backtrack(i + 1, path + s[i].swapcase())
        backtrack(0, "")
        return res