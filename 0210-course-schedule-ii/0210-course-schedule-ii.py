class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        graph = [[] for i in range(n)]
        inward = [0 for i in range(n)]
        q = deque()
        Sorted = []

        for c , p in prerequisites:
            graph[p].append(c)
            inward[c] += 1
        for i in range(n):
            if inward[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            Sorted.append(curr)
            inward[curr] -= 1

            for course in graph[curr]:
                inward[course] -= 1
                if inward[course] == 0:
                    q.append(course)
        
        if len(Sorted) != n:
            return []
        
        return Sorted



