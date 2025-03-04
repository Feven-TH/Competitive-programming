class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        rabbits = 0
        for key,val in counts.items():
            if val > key + 1:
                rabbits += math.ceil(val / (key + 1)) * (key +1)
            else:
                rabbits += key + 1
        return rabbits