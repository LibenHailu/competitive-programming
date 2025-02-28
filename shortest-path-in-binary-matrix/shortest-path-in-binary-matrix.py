class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        DIRS = [(r, c) for r in range(-1, 2) for c in range(-1, 2)]
        queue = collections.deque([(0,0,1)])
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        m = len(grid[0])
        while queue:
            r, c, count = queue.popleft()
            if r == n - 1 and c == m - 1:
                return count 
            
            for dr, dc in DIRS:
                new_r, new_c = r + dr, c + dc
                if inbound(new_r,new_c) and (new_r,new_c) not in visited and not grid[new_r][new_c]:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, count + 1))
                                  
        return -1