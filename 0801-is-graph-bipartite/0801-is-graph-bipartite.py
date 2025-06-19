class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited = [-1]* len(graph)


        def dfs(node):
            temp = True

            for ni in graph[node]:
                if visited[ni] == -1:
                    visited[ni] = 1 - visited[node]
                    if not dfs(ni):
                        return False
                else:
                    temp = temp and visited[ni] != visited[node]

            return temp

       
        for i in range(len(graph)):
            if visited[i] == -1:
                visited[i] = 0

            if not dfs(i):
                return False
        
        return True
            



        




                







