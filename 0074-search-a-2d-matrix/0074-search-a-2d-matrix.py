class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low , Low = 0 , 0
        high, High = len(matrix) - 1 , len(matrix[-1]) - 1

        while low <= high:
            mid = (low + high)//2
            midd = (Low + High)//2
            
            if matrix[mid][midd] == target:
                return True

            if matrix[mid][midd] > target:
                if matrix[mid][Low] <= target <= matrix[mid][High]:
                    High = midd - 1
                else:
                    high = mid - 1
                    Low , High = 0 , len(matrix[0]) - 1
                   
            if matrix[mid][midd] < target:
                if matrix[mid][Low] <= target <= matrix[mid][High]:
                    Low = midd + 1
                else:
                    low = mid + 1
                    Low , High = 0 , len(matrix[0]) - 1 
        return False