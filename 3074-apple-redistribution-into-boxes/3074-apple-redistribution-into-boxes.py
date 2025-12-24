class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse= True)
        c = 0
        apples = sum(apple)
        for x in capacity:
            if apples <= 0:
                return c
            apples -= x
            c += 1
        return c