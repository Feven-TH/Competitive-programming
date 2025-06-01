class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = arr[-1]
        res = [-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            # print(i,i-1)
            maxx = max(maxx,arr[i])
            res[i-1] = maxx
        res[-1] = -1
        return res
