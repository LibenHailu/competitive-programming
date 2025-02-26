class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = [i for i in range(size)]
    
    def find(self, x):
        while self.root[x] != x:
            x = self.find(self.root[x])
        return self.root[x]
    def union(self, x1,x2):
        parent1, parent2 = self.find(x1), self.find(x2)
        if self.rank[parent1] > self.rank[parent2]:
            self.root[parent2] = self.root[parent1]
        elif self.rank[parent1] < self.rank[parent2]:
            self.root[parent1] = self.root[parent2]
        else:
            self.root[parent1] = self.root[parent2]
            self.rank[parent1] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        uf = UnionFind(n)
        numberOfComponents = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfComponents -= 1
                    uf.union(i, j)

        return numberOfComponents