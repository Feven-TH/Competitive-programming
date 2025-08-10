class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr,x)
        i,j = ind-1, ind
        res = []
        while k > 0:
            if i < 0:
                res.append(arr[j])
                j += 1
            elif j >= len(arr):
                res.append(arr[i])
                i -= 1
            elif abs(arr[i] - x) <= abs(arr[j] - x):
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
            k -= 1

        return sorted(res)
                
