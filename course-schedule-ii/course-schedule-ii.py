class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []
        
