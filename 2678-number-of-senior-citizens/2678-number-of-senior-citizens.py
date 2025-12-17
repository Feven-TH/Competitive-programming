class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for d in details:
            if int(d[11:13]) > 60:
                c += 1
        return c