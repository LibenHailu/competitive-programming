class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.find(self.parent[x])
        return self.parent[x]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False 
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = self.parent[parent1]
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = self.parent[parent2]
        else:
            self.rank[parent1] += 1
            self.parent[parent1] = self.parent[parent2]
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for node1, node2 in edges:
            if not uf.union(node1, node2):
                return False
            n -= 1
        return n == 1
            