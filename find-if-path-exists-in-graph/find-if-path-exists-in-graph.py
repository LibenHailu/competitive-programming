class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visited = set()
        stack = [source]
        visited.add(source)
        while stack:
            node = stack.pop()
            if node == destination:
                return True    
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        return False
        
        