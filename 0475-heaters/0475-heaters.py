class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        maxx = 0

        for h in houses:
            i = bisect_left(heaters, h)
            left = abs(h - heaters[i - 1]) if i > 0 else float('inf')
            right = abs(h - heaters[i]) if i < len(heaters) else float('inf')

            minn = min(left , right)
            maxx = max(maxx, minn)
        return maxx
        