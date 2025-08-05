class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        flag = [False]*len(fruits)
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit and flag[i] == False :
                    flag[i] = True
                    break
        return sum(1 for f in flag if f == False) 
        
