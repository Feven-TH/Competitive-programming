class Trie(object):
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.ends = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in words:
            self.insert(root, word)
        q = deque([(root,"")])
        res = ""
        while q:
            node, curr = q.popleft()
            if len(res) < len(curr):
                res = curr
            for i in range(26):
                if node.children[i] and node.children[i].ends:
                    ch = chr(i + ord('a'))
                    nxt = curr + ch 
                    q.append((node.children[i], nxt))
        return res
        
    def insert(self, root, word):
        curr = root
        for ch in word:
            i = ord(ch) - ord('a')  
            if not curr.children[i]:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.ends = True

