class Trie(object):
    def __init__(self):
        self.ends = False
        self.children = [None for i in range(26)]

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        def insert(word, root):
            curr = root
            for ch in word:
                i = ord(ch) - ord('a')
                if not curr.children[i]:
                    curr.children[i] = Trie()
                curr = curr.children[i]
            curr.ends = True
       
        for w in dictionary:
            insert(w, root)

        s = list(sentence.split(' '))
        
        for i in range(len(s)):
            word = s[i]
            curr = root
            for j,ch in enumerate(word):
                ind = ord(ch) - ord('a')
                if not curr.children[ind]:
                    break
                curr = curr.children[ind]    
                
                if curr.ends:
                    s[i] = word[:j+1]
                    break
       
        return ' '.join(s)
        