class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool: 
        def helper(l ,r , p1 , p2 , turn1):
            if l == r:
                if turn1:
                    return p1 + nums[l] >= p2
                else:
                    return p1 >= p2 + nums[l]
            
            if turn1:
                left = helper(l + 1, r , p1 + nums[l] , p2 , not turn1)
                right = helper(l, r -1  , p1 + nums[r] , p2 , not turn1)
                return left or right
            else:
                left = helper(l + 1, r , p1  , p2 + nums[l] , not turn1)
                right = helper(l, r -1  , p1 , p2 + nums[r]  , not turn1)
                return left and right

        return helper(0, len(nums) - 1, 0 , 0 ,True)
            


            