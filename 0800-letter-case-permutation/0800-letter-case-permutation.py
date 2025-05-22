class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        chars = [i for i, c in enumerate(s) if c.isalpha()]
        res = []
        for i in range(1<<len(chars)):
            temp = list(s)
            for j in range(len(chars)):
                idx = chars[j]
                if i & (1<<j):
                    temp[idx] = temp[idx].swapcase()
            res.append("".join(temp))
        return res            

            