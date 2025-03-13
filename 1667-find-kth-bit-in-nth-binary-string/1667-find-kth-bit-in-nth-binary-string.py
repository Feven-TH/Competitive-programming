class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            inverted = ""
            for b in s:
                if b == "0":
                    inverted += "1"
                else:
                    inverted += "0"
            return inverted[::-1]
            
        def helper(n):
            if n == 1:
                return "0"
            else:
                temp = helper(n - 1)
                # print(temp)
                # print(invert(temp))
                return temp + "1" + invert(temp)
                
        return helper(n)[k - 1]
