class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def check(n):
            divs = set() 
            for i in range(1, int(n**0.5)+1): 
                if n % i == 0: 
                    divs.add(i) 
                    divs.add(n//i) 
            return sum(divs) if len(divs) == 4 else 0
        
        res = 0
        for num in nums:
            res += check(num)
        return res
