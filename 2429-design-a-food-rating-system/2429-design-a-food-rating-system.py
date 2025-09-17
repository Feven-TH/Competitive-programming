class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.info = {}
        self.heaps = defaultdict(list)
        for f,c,r in zip(foods,cuisines,ratings):
            self.info[f] = [c,r]
            heappush(self.heaps[c], (-r,f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.info[food]
        self.info[food][1] = newRating
        heappush(self.heaps[cuisine], (-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while heap:
            rating, food = heap[0]   
            if -rating == self.info[food][1]:
                return food
            heappop(heap)  
        return ""



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)