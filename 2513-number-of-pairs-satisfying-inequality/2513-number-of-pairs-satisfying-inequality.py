class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        temp = [nums1[i] - nums2[i] for i in range(len(nums1))]
        count = 0
        def merge(left , right):
            i , j = 0 , 0
            Sorted = []
            nonlocal count

            while i < len(left) and j < len(right):
                if left[i] <= right[j] :
                    Sorted.append(left[i])
                    i += 1
                else:
                    Sorted.append(right[j]) 
                    j += 1
            while i < len(left):
                Sorted.append(left[i]) 
                i += 1
            while j < len(right):
                Sorted.append(right[j]) 
                j += 1

            l , r = 0 , 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r] + diff:
                    count += len(right) - r
                    l += 1
                else:
                    r += 1
            return Sorted 

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]] 
            
            mid = (left + right) // 2
            Left = mergeSort(left, mid, arr)
            Right = mergeSort(mid + 1, right, arr)

            return merge(Left , Right)
        mergeSort(0 , len(temp) - 1 ,temp)    
        return count