class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = [[] for i in range(n)]
        indegree = [0 for i in range(n)]
        q = deque()
        pre = defaultdict(set)
        res = []

        for p , c in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                pre[nei].add(curr)
                for n in pre[curr]:
                    pre[nei].add(n)

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        for u,v in queries:
            res.append(u in pre[v])
            
        return res


        