class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topsort(graph,indegree,nodes):
            res = []
            queue = deque()
            for node in nodes:
                if indegree[node] == 0:
                    queue.append(node)
            while queue:
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res if len(res) == len(nodes) else []

        
        newG = m
        for i in range(n):
            if group[i] == -1:
                group[i] = newG
                newG += 1
        newM = newG
        itemsGraph = defaultdict(list)
        items_indegree = [0]*n
        
        groupsGraph = defaultdict(list)
        groups_indegree = [0]*newM

        groupings = defaultdict(list)

        for i in range(n):
            curr_group = group[i]
            groupings[curr_group].append(i)

            for b in beforeItems[i]:
                b_group = group[b]
                if b_group == curr_group:
                    itemsGraph[b].append(i)
                    items_indegree[i] += 1
                else:
                    groupsGraph[b_group].append(curr_group)
                    groups_indegree[curr_group] += 1

        group_node = list(range(newM))
        group_order = topsort(groupsGraph, groups_indegree, group_node)  
        if not group_order:
            return []

        ans = []
        for g in group_order:
            items = groupings[g]
            if not items:
                continue
            item_order = topsort(itemsGraph, items_indegree,items) 
            if not item_order:
                return []
            ans.extend(item_order)
        return ans


