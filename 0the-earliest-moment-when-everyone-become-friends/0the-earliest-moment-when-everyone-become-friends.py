class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.size = size
        self.rank = [1] * size 
    
    def find(self, x):
        while x != self.root[x]:
            x = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False 
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.rank[root_x] += 1
            self.root[root_x] = root_y
        self.size -= 1
        if self.size == 1:
            return True
        return False
            
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for time, node1, node2 in logs:
            if uf.union(node1,node2):
                return time
        return -1
        