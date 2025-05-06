class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {chr(i): chr(i) for i in range(97, 123)}
        rank = {chr(i): 0 for i in range(97, 123)}
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    root[rooty] = rootx  
                elif rank[rootx] < rank[rooty]:
                    root[rootx] = rooty
                else:
                    root[rooty] = rootx
                    rank[rootx] += 1
        
        for eq in equations: 
            if eq[1:3] == "==":
                print(eq[0], eq[-1])
                print("parents" , find(eq[0]), find(eq[-1]))
                union(eq[0], eq[-1])
        for eq in equations: 
            if eq[1:3] == "!=" and find(eq[0]) == find(eq[-1]):
                    return False
        # print(root)
        return True