class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m = len(strs), len(strs[0])
        is_sorted = [False]*(n-1)
        res = 0
        for j in range(m):
            flag = True
            for i in range(n-1):
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    flag = False
                    break
            if flag:
                for i in range(n-1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
            else:
                res += 1
        return res


