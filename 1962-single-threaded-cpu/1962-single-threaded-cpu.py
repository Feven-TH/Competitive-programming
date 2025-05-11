class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        Tasks = sorted([(enq, proc, i) for i,(enq,proc) in enumerate(tasks)])
        res = []
        minn = []
        time, ind = 0 ,0
        
        while len(res) < len(tasks):
            while ind < len(tasks) and Tasks[ind][0] <= time:
                heappush(minn, (Tasks[ind][1], Tasks[ind][2])) 
                ind += 1
            if minn:  
                proc,i = heappop(minn)
                res.append(i)
                time += proc
            else:  
                time = Tasks[ind][0]
        
        return res
