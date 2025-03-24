class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(curr):
            if len(curr) == n:
                res.append(''.join(str(i) for i in curr))
                return
            
            for i in range(2):
                if i == 0 and curr and curr[-1] == 0:
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return res