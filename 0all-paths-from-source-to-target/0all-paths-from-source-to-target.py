class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def backtrack(node, curr):
            if node == len(graph) - 1:
                res.append(curr[:])
                return 
            for nei in graph[node]:
                curr.append(nei)
                backtrack(nei, curr)
                curr.pop()
        backtrack(0, [0])
        return res