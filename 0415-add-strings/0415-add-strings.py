class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        rem = 0
        i,j = len(num1) -1 , len(num2) -1

        while i >= 0 or j >= 0 or rem:
            x = num1[i] if i >= 0 else 0
            y = num2[j] if j >= 0 else 0
            summ = int(x) + int(y) + rem
            rem = summ//10
            res += str(summ % 10)

            i -= 1
            j -= 1
        return res[::-1]

        