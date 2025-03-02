class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        visited = set()
        indegrees = [0] * n 
        graph = defaultdict(list)
        for src, dst in relations:
            graph[src - 1].append(dst - 1)
            indegrees[dst - 1] += 1
        
        queue = deque([])
        for index, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(index)
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for nei in graph[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)
        return count if len(visited) == n else -1
            