class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        MOD = 10**9 + 7

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        heap = [(0,0)]
        # visited = set()
        shtime = [float('inf')] * n
        shtime[0] = 0 

        pathCount = [0] * n
        pathCount[0] = 1  

        while heap:
            time, node = heappop(heap)

            if time > shtime[node]:
                continue

            for ni,wh in graph[node]:
                if time + wh < shtime[ni]:
                    shtime[ni] = time + wh
                    pathCount[ni] = pathCount[node]
                    heappush(heap,(time + wh, ni))
                elif time + wh == shtime[ni]:
                    pathCount[ni] = (pathCount[ni] + pathCount[node]) % MOD

        return pathCount[n - 1]