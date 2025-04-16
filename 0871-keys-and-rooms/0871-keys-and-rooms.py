class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = deque()
        q.append(rooms[0])
        while q:
            curr = q.popleft()
            for neigh in curr:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(rooms[neigh])
            if len(visited) == len(rooms):
                return True
        return False

        
