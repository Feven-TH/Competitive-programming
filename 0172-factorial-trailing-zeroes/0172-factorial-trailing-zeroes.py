class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * (factorial(n - 1))

        num = factorial(n)
        # print(s)
        count = 0
        while num % 10 == 0:
            count += 1
            num = num // 10
        return count
         