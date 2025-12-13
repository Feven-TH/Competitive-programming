class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        active = []
        valid = set(["electronics", "grocery", "pharmacy", "restaurant"])
        
        def check(s):
            return bool(s) and all(ch.isalnum() or ch == "_" for ch in s)
        
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in valid and check(code[i]):
                active.append([code[i],businessLine[i]])
        
        active.sort(key = lambda x: (x[1], x[0]))
        return [x for x,y in active]