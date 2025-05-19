class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n , m = len(nums1), len(nums2)
        res = 0
        if n%2 == 0 and m%2 == 1:
            for num in nums1:
                res ^= num
        elif n%2 == 1 and m%2 == 0:
            for num in nums2:
                res ^= num
        elif n%2 == 1 and m%2 == 1:
            nums1.extend(nums2)
            for num in nums1:
                res ^= num
        return res



        
        print()           


