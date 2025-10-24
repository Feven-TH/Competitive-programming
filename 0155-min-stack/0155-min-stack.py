class MinStack:
    def __init__(self):
        self.stack = [(float("inf"), float("inf"))]
    def push(self, val):
        last_min = self.stack[-1][1] # last minimum value
        new_min = min(val, last_min)
        self.stack.append((val, new_min))
    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()
    def top(self):
        if len(self.stack) <= 1:
            return None
        return self.stack[-1][0]
    
    def getMin(self):
        if len(self.stack) <= 1:
            return None
        return self.stack[-1][1]