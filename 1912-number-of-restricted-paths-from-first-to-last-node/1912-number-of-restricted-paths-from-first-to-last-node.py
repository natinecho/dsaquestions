class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        MOD = 10**9 + 7

        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        distance = [float("inf") for i in range(0,n + 1)]

        distance[n] = 0

        heap = [(0,n)]

        while heap:
            dis , node = heappop(heap)
            
            if dis > distance[node]:
                continue

            for ni, wh in graph[node]:
                if dis + wh < distance[ni]:
                    distance[ni] = dis + wh
                    heappush(heap,(distance[ni] , ni))

        dp = [-1] * (n + 1)

        def back(node):

            if node == n:
                return 1

            if dp[node] != -1:
                return dp[node]
            
            ans = 0
            for ni,wh in graph[node]:
                if distance[node] > distance[ni]:
                    ans = (ans + back(ni)) % MOD

            dp[node] = ans

            return dp[node]

        
        return back(1)