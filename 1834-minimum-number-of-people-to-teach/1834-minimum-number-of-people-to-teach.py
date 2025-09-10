class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = {i+1: set(l) for i,l in enumerate(languages)}
        broken = []
        for u,v in friendships:
            if langs[u].intersection(langs[v]) == set():
                broken.append((u,v))

        if not broken:
            return 0

        users = set()
        for u,v in broken:
            users.add(u)
            users.add(v)
        ans = float("inf")
        for lang in range(1, n+1):
            cnt = 0
            for user in users:
                if lang not in langs[user]:
                    cnt+= 1
            ans = min(ans, cnt)

        return ans