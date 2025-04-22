class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        maps = defaultdict(list)
        for i,num in enumerate(manager):
            if num != -1:
                maps[num].append(i)
        
        maxx = 0 
        def dfs(node , time):
            nonlocal maxx
            if not maps[node]:
                maxx = max(maxx , time)
                return time
            for subs in maps[node]:
                dfs(subs, time + informTime[subs])   
            return time 

        dfs(headID , informTime[headID])
        return maxx
        