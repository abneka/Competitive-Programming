class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        dep_graph = defaultdict(int)
        
        for recipe, ingredient in zip(recipes, ingredients):
            for ingrs in ingredient:
                dep_graph[recipe] += 1
                graph[ingrs].append(recipe)
        
        visited = set()
        queue = deque(supplies)
        recipes = set(recipes)
        ans = []
        
        while queue:
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            visited.add(node)

            for ingrs in graph[node]:
                dep_graph[ingrs] -= 1
                if ingrs not in visited and not dep_graph[ingrs]:
                    queue.append(ingrs)
        
        return ans
            