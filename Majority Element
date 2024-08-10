class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_count = {}
        for num in nums:
            if num in element_count:
                element_count[num]+=1
            else:
                element_count[num]=1
        ans=[]
        for element,count in element_count.items():
            if count > len(nums)//3:
                ans.append(element)
        return ans
