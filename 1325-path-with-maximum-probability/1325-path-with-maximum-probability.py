class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        
        for i in range(len(edges)):
            u,v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        que = [(-1, start_node)]
        visited = set()

        while que:
            time, node = heappop(que)
            time = -1 * time
            visited.add(node)
            if node == end_node:
                return time

            for ni, wh in graph[node]:
                if ni not in visited:
                    heappush(que, ( -1 *(wh * time), ni))


        return 0