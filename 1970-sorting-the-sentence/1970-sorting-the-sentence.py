class Solution:
    def sortSentence(self, s: str) -> str:
        sentence=s.split()
        Sorted = sorted(range(len(sentence)), key=lambda i:sentence[i][-1])
        res=[sentence[j][:-1] for j in Sorted]   
        return ' '.join(res)    