class DataStream:

    def __init__(self, value: int, k: int):
        self.stack = []
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        self.num = num
        if self.num == self.value:
            self.stack.append(self.num)
        else:
            self.stack = []

        return len(self.stack) >= self.k




    

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)