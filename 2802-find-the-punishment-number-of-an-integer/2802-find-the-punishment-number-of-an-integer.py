class Solution:
    def punishmentNumber(self, n: int) -> int:
        def part(square, num):
            def backtrack(index, curr):
                if index == len(square):
                    return curr == num

                for end in range(index + 1, len(square) + 1):
                    sub = square[index:end]
                    val = int(sub)

                    if len(sub) > 1 and sub[0] == "0" :
                        continue
                    if backtrack(end, curr + val):
                        return True
                return False
            return backtrack(0, 0)

        summ = 0
        for i in range(1, n + 1):
            square = str(i * i)
            if part(square, i):
                summ += i * i

        return summ
