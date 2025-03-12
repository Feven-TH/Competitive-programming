class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = [0] * len(deck)
        queue = deque(range(len(deck)))
        deck.sort()

        for d in deck:
            index = queue.popleft()
            res[index] = d
            if queue:
                queue.append(queue.popleft())
                
        return res
        

