class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1,60):
            T = num1 - k*num2
            if T <0:
                continue
            if bin(T).count('1') <= k<=T:
                return k
        return -1
             
