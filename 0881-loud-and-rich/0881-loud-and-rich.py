class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for i in range(len(quiet))]
        incoming = [0] * len(quiet)
        q = deque()
        res = [i for i in range(len(quiet))]

        for r ,p in richer:
            graph[r].append(p)
            incoming[p] += 1
        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                if quiet[res[curr]] < quiet[res[nei]]:
                    res[nei] = res[curr]
                
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)
        
        return res

        # res = []
        # for i in range(len(quiet)):
        #     minn = float('inf')
        #     ind = -1
        #     for j in range(i,len(quiet)):
        #         if quiet[ranked[j]] < minn:
        #             minn = quiet[ranked[j]]
        #             ind = ranked[j]
        #             # print("minn:" ,minn)
        #             # print("ind:" , ind)
        #     res.append(ind)
        # return res
        
       