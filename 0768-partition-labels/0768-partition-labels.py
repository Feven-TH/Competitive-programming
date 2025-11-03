class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        maps = {}
        for i,ch in enumerate(s):
            maps[ch] = i
        maxx = 0
        res = []
        start = 0
        for i,ch in enumerate(s):
            maxx = max(maxx,maps[ch])
            if i == maxx:
                res.append(i-start+1)
                start = i+1
        return res