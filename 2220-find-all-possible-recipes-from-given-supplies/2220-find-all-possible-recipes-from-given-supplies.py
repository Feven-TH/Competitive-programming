class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                incoming[recipes[i]] += 1
      
        q = deque(supplies)
        res = []

        while q:
            curr = q.popleft()
            if curr in recipes:
                res.append(curr)
                
            for recipe in graph[curr]:
                incoming[recipe] -= 1
                if incoming[recipe] == 0:
                    q.append(recipe)
            
        return res

                    
      
        
