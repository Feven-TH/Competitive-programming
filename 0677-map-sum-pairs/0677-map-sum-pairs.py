class MapSum:

    def __init__(self):
        self.children = [None for i in range(26)]
        self.value = None
        self.ends = False

    def insert(self, key: str, val: int) -> None:
        curr = self
        for ch in key:
            i = ord(ch) - ord('a')
            if not curr.children[i]:
                curr.children[i] = MapSum()
            curr = curr.children[i]         
        curr.ends = True
        curr.value = val

    def sum(self, prefix: str) -> int:
        summ = 0 
        def dfs(curr):
            nonlocal summ
            if curr.ends:
                summ += curr.value
            for i in range(26):
                if curr.children[i]:
                    dfs(curr.children[i])
            return summ
        
        curr = self
        for ch in prefix:
            i = ord(ch) - ord('a')
            if not curr.children[i]:
                return 0
            curr = curr.children[i]
        return dfs(curr)
        
        
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)