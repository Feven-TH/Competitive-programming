class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_G = [-1] * len(nums1)
        maps = {nums1[i] : i for i in range(len(nums1))}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                if nums2[index] in nums1:
                    next_G[maps[nums2[index]]] = nums2[i]
            stack.append(i)
        return next_G