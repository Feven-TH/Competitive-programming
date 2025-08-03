class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        maxx = 0
        left = 0
        total = 0

        for r in range(n):
            total += fruits[r][1]

            while left <= r:
                L = fruits[left][0]
                R = fruits[r][0]

                cost1 = abs(startPos - L) + (R-L)
                cost2 = abs(R - startPos) + (R-L)

                if min(cost1, cost2) <= k:
                    break
                total -= fruits[left][1]
                left += 1

            maxx = max(maxx, total)

        return maxx