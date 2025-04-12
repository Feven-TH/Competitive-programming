class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set(edges[i][1] for i in range(len(edges)))
        res = []
        for i in range(n):
            if i not in losers:
                res.append(i)
        if len(res) == 1:
            return res[0]
        else:
            return -1