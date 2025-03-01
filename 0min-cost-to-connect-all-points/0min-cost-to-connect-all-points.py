class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((j, distance))
                graph[j].append((i, distance))
        
        heap = [(0, 0)]
        visited = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for nei, nei_cost in graph[node]:
                heapq.heappush(heap, (nei_cost, nei))
        return res
        
        
        
        
        
        
        