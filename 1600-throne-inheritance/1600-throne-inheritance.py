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
        def dfs(start, path):
            for child in self.kingdom[start]:
                if not child in self.cementery:
                    path.append(child)
                dfs(child, path)
                
            return path
        
        path = []
        if not self.king in self.cementery:
            path.append(self.king)
        return dfs(self.king, path)
                


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()