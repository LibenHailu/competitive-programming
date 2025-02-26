class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.connected_components = size
    def find(self, x):
        while self.parent[x] != x:
            x = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x1, x2):
        parent1, parent2 = self.find(x1), self.find(x2)
        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.rank[parent1] += 1
            self.parent[parent1] = parent2
        self.connected_components -= 1
        
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x1, x2 in edges:
            uf.union(x1, x2)
        return uf.connected_components