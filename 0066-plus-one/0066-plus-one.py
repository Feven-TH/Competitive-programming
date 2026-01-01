class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num= num*10 + i
        return list(map(int, str(num+1)))
       