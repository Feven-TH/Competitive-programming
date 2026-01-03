class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        maps = defaultdict(int)
        MOD = 10**9 + 7
        for x,y in points:
            maps[y] += 1
        sides = [] 
        for p in maps.values():
            if p >= 2:
                sides.append(math.comb(p,2))
        
        summ = sum(sides)
        squares = sum(s*s for s in sides)
        res = (summ**2 - squares)//2
        return res%MOD
        