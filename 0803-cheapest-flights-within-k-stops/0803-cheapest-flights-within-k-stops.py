class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
            # graph[v].append((u,w))

        que = [(0,0,src)]
        visited = {}

        while que:
            price,level,node = heappop(que)
            if node == dst and level <= k + 1:
                return price

            if level > k:
                continue

            if node not in visited or visited[node] > level:
                visited[node] = level

                for ni,wh in graph[node]:
                    heappush(que,(price + wh , level + 1,ni))


        return -1