class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((time, dst))
        heap = [(0, k)]
        visited = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            
            if node in visited: continue 
            res = max(res, cost)
            visited.add(node)
            for nei_cost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (cost + nei_cost, nei))
        return res if len(visited) == n else -1
            