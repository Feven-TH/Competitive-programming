class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        maps = [[] for _ in range(len(graph))]
        incomings = [0 for _ in range(len(graph))]

        for i, neigh in enumerate(graph):
            for n in neigh:
                maps[n].append(i)
            incomings[i] = len(neigh)

        q = deque([])
        for i in range(len(incomings)):
            if incomings[i] == 0:
                q.append(i)
        
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for neigh in maps[curr]:
                incomings[neigh] -= 1
                if incomings[neigh] == 0:
                    q.append(neigh)
                    
        order.sort()
        return order
       