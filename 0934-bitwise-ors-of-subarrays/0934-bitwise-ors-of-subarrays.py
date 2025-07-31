class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        seen = set()
        curr = set()
        for n in arr:
            curr = {n | x for x in curr}|{n}
            seen |= curr
        return len(seen)