class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]*len(arr)
        for i in range(1,len(arr)):
            prefix[i] = prefix[i-1]^arr[i]
        
        res = []
        for q in queries:
            i,j = q
            temp = prefix[j]
            if i>0:
                temp ^= prefix[i-1]
            res.append(temp)
            
        return res