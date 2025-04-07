class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        maps = defaultdict(set)
        for i,j in trust:
            maps[i].add(j)
        trusted = []
        for val in maps.values():
            for v in val:
                trusted.append(v)
        for i in range(1, n+1):
            if i not in maps and trusted.count(i) == n - 1:
                return i
        return -1
