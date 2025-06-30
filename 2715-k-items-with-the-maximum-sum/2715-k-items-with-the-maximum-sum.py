class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        summ = 0
        summ += min(k,numOnes)
        k -= summ
        k -= min(k,numZeros) 
        summ -= min(k,numNegOnes)
        return summ



