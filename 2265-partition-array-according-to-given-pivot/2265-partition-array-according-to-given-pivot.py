class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1 = []
        arr2 = []
        count = 0 
        for num in nums:
            if num < pivot:
                arr1.append(num)
            elif num > pivot:
                arr2.append(num)
            else:
                count += 1
        arr1.extend(count*[pivot])
        return arr1 +arr2
