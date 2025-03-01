class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
    
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
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1
        return True
         
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all_distances = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_distances.append((distance, i, j))
            
        all_distances.sort()
        res = 0
        uf = UnionFind(n)
        for dist, node1, node2 in all_distances:
            if uf.union(node1, node2):
                res += dist
        
        return res