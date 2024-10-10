class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = [[float("inf")] *numCourses  for _ in range(numCourses)]

        for i in range(numCourses):
            graph[i][i] = 0

        for  u,v in prerequisites:
            graph[u][v] = 1
            # graph[v][u] = 1

        for i in range(numCourses):        
            for u in range(numCourses):        
                for v in range(numCourses):
                    graph[u][v] = min(graph[u][v],graph[u][i] + graph[i][v])


        ans = []

        for u,v in  queries:
            ans.append(graph[u][v] != float("inf"))     

        
        return ans