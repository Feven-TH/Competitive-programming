class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        cases = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in cases:    
                cases[lw] = w

        def devowel(word: str) -> str:
            return "".join('*' if c in 'aeiou' else c for c in word.lower())

        vowel_map = {}
        for w in wordlist:
            vw = devowel(w)
            if vw not in vowel_map:   
                vowel_map[vw] = w

        ans = []
        for q in queries:
            if q in words:                  
                ans.append(q)
            elif q.lower() in cases:        
                ans.append(cases[q.lower()])
            elif devowel(q) in vowel_map:        
                ans.append(vowel_map[devowel(q)])
            else:                                 
                ans.append("")
        return ans
