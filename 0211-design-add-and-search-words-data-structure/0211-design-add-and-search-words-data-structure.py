class WordDictionary:
    def __init__(self):
        self.ends = False
        self.children = [None for _ in range(26)]
    
    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            i = ord(ch) - ord('a')
            if not curr.children[i]:
                curr.children[i] = WordDictionary()
            curr = curr.children[i]
        curr.ends = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] == '.':
                for ch in curr.children:
                    if ch and ch.search(word[i+1:]):
                        return True
                return False
            else:
                if not curr.children[ord(word[i]) - ord('a')]:
                    return False
                curr = curr.children[ord(word[i]) - ord('a')]      
        return curr.ends



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)