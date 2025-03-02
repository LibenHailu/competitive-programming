class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        destinations = [float("inf")] * n
        destinations[src] = 0
        for _ in range(k + 1):
            temp = destinations[:]
            for u, v, w in flights:
                if destinations[u] != float("inf"):
                    temp[v] = min(temp[v],destinations[u] + w)
            destinations = temp
        return destinations[dst] if destinations[dst] != float("inf") else -1
#         adj = defaultdict(list)
#         for u, v, w in flights:
#             adj[u].append((v, w))
        
#         stops = [float('inf')] * n
#         pq = [(0, src, 0)] 
        
#         while pq:
#             cost, node, steps = heapq.heappop(pq)
            
#             if steps > stops[node] or steps > k + 1:
#                 continue
            
#             stops[node] = steps
            
#             if node == dst:
#                 return cost
            
#             for neighbor, price in adj[node]:
#                 heapq.heappush(pq, (cost + price, neighbor, steps + 1))
                
#         return -1
