class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for i in range(1,n):
            graph[i- 1].append(i)
        
        def bfs():
            que = deque([(0,0)])
            visited = set()

            while que:
                node,level = que.popleft()

                if node == n - 1:
                    return level


                for ni in graph[node]:
                    if ni not in visited:
                        visited.add(ni)
                        que.append((ni,level + 1))
            
            return 0
        

        ans = []

        for u,v in queries:
            graph[u].append(v)

            ans.append(bfs())


        return ans
