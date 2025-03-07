class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackA = []
        stackB = []
        for c in s:
            if stackA and c == "#":
                stackA.pop()
            if c != '#':
                stackA.append(c)
        for T in t:
            if stackB and T == "#":
                stackB.pop()
            if T != '#':
                stackB.append(T)
        
        return stackA == stackB