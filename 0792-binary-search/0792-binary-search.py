class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def Search(l,h):
            mid = (l + h)//2
            if l > h:
                return -1
            if nums[mid] == target:
                return mid      
            elif nums[mid] > target:
                return Search(l , mid - 1)
            else:
                return Search(mid + 1 , h)
        return Search(0, len(nums) - 1)
                  