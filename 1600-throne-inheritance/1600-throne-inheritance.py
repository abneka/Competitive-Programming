class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.kingdom = defaultdict(list)
        self.cementery = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.cementery.add(name)

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        order = []
        
        def dfs(start):
            if start not in visited and start not in self.cementery:
                visited.add(start)
                order.append(start)
            
            for child in self.kingdom[start]:
                if not child in visited:
                    dfs(child)
        
        dfs(self.king)
        return order
                


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()