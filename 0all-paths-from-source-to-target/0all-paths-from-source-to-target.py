class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        queue = collections.deque([(0, [0])])
        visited = set()
        while queue:
            node, path = queue.popleft()
            if node == len(graph) - 1:
                res.append(path)
                continue 
            
            for nei in graph[node]:
                # if nei not in visited:
                queue.append((nei, path + [nei] ))
        return res
        # res = []
        # def backtrack(node, curr):
        #     if node == len(graph) - 1:
        #         res.append(curr[:])
        #         return 
        #     for nei in graph[node]:
        #         curr.append(nei)
        #         backtrack(nei, curr)
        #         curr.pop()
        # backtrack(0, [0])
        # return res
        