class Trie(object):
    def __init__(self):
        self.children = [None for i in range(26)]
        self.ends = False
        self.count = 0 

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        def insert(root,word):
            curr = root
            for ch in word:
                i = ord(ch) - ord('a')
                if not curr.children[i]:
                    curr.children[i] = Trie()
                curr = curr.children[i]
                curr.count += 1
            curr.ends = True

        for word in words:
            insert(root,word)
        
        res = []
        for word in words:
            score = 0
            curr = root
            for ch in word:
                i = ord(ch) - ord('a')
                curr = curr.children[i]
                score += curr.count
            res.append(score)
        return(res)
        