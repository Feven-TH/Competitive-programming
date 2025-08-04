class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maps = defaultdict(int)
        maxx = 0
        j = 0
        for i in range(len(fruits)):
            maps[fruits[i]] += 1
            while len(maps) > 2:
                maps[fruits[j]] -= 1
                if maps[fruits[j]] == 0:
                    del maps[fruits[j]]
                j += 1
            maxx = max(maxx, i- j +1) 
        return maxx

