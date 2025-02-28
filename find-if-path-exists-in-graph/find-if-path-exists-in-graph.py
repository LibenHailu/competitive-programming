class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visited = set()
        visited.add(source)
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for child in adj[node]:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
        return False
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     for nei in adj[node]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             if dfs(nei):
        #                 return True
        #     return False
        # return dfs(source)
#         stack = [source]
#         visited.add(source)
#         while stack:
#             node = stack.pop()
#             if node == destination:
#                 return True    
#             for nei in adj[node]:
#                 if nei not in visited:
#                     visited.add(nei)
#                     stack.append(nei)
        
#         return False
        
        