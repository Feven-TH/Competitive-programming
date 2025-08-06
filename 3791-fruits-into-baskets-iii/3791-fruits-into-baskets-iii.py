class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = int(sqrt(n)) +1
        blocks = [baskets[i:i+m] for i in range(0,n,m)]
        maxx = [max(block) for block in blocks]
        res = 0

        for fruit in fruits:
            flag = False
            for ind in range(len(blocks)):
                if maxx[ind] < fruit:
                    continue
                for i in range(len(blocks[ind])):
                    if blocks[ind][i] >= fruit:
                        blocks[ind][i] = 0 
                        maxx[ind] = max(blocks[ind])  
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                res += 1
        return res
                
    
    