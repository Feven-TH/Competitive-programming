class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                curr = accounts[i][j]
                graph[curr].append(i)

        n = len(accounts)
        parent = {i: i for i in range(n)}  
        rank = {i: 0 for i in range(n)}  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                elif rank[rooty] > rank[rootx]:
                    parent[rootx] = rooty
                else:
                    parent[rootx] = rooty
                    rank[rooty] += 1

       
        for key, vals in graph.items():
            for i in range(1, len(vals)):
                head = vals[0]
                union(head, vals[i])

        merged = defaultdict(set)  
        for i, account in enumerate(accounts):
            root = find(i)
            merged[root].update(account[1:]) 

        result = []
        for root, emails in merged.items():
            name = accounts[root][0]  
            result.append([name] + sorted(emails))  
        return result
