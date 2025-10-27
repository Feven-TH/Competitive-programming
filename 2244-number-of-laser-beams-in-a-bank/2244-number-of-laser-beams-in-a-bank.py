class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [row.count('1') for row in bank if row.count('1') > 0]
        total= 0
        for i in range(1,len(counts)):
            total += counts[i-1]*counts[i]
        return total