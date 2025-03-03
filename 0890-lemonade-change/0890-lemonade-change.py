class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10 and fives > 0:
                tens += 1
                fives -= 1
            elif i == 20 and fives > 0 and tens > 0:
                tens -= 1
                fives -= 1
            elif i == 20 and fives > 2 and tens == 0:
                fives -= 3
            else:
                return False
        return True
