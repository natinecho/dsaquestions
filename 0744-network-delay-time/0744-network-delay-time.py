class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maxx = 0

        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((v, w))

        que = [(0, k)]
        visited = set()
        maxx = -inf

        while que:
            time, node = heappop(que)
            # print(time)
            visited.add(node)
            if len(visited) == n:return time

            for ni, wh in graph[node]:
                if ni not in visited:
                    heappush(que, ( wh + time, ni))
                    # visited.add(ni)



        return -1 

        