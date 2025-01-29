class UnionFind:
    def __init__(self,size):
        self.root = {i:i for i in range(1,size + 1)}
        self.size = [0] * (size + 1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
     
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
        else:
            return False
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        obj = UnionFind(len(edges))
        for i,j in edges:
            
            if not obj.union(i,j):
                return [i,j]
            
        