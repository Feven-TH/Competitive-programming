class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(path,ind,target):
            if target == 0:
                res.append(path[:])
                return 
            if target <0:
                return 
            for i in range(ind,len(candidates)):
                path.append(candidates[i])
                backtrack(path, i, target-candidates[i])
                path.pop()
        backtrack([],0,target)
        return res
            
