class DataStream:

    def __init__(self, value: int, k: int):
        self.counts = 0
        self.value = value
        self.k = k
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.counts += 1
        else:
            self.counts = 0

        return self.counts >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)