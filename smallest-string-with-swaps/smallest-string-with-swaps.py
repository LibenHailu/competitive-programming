class Unionfind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = list(range(size))
    
    def find(self, x):
        while self.root[x] != x:
            x = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y  = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.rank[root_y] += 1
            self.root[root_x] = root_y

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = Unionfind(len(s))
        for x, y in pairs:
            uf.union(x, y)
        res = [''] * len(s)
        root_to_component = defaultdict(list)
        for i in range(len(s)):
            root = uf.find(i)
            root_to_component[root].append(i)
        
        for  _, indices in root_to_component.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)
        
            for c,i in zip(chars,indices):
                res[i] = c
        return "".join(res)
        
        