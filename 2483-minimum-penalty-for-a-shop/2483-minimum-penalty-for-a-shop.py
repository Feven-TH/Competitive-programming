class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        suff,pre = customers.count("Y"), 0
        best_time, minn = 0, suff
        for i in range(n):
            if customers[i] == "Y":
                suff -= 1
            else:
                pre += 1
            
            pen = suff + pre
            if minn > pen:
                best_time = i + 1
                minn = pen
        return best_time 