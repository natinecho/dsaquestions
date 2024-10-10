class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        dist = [float("inf")]*n
        dist[0] = 0

        visited = set()

        for u,v,lenn in edges:
            graph[u].append((v,lenn))        
            graph[v].append((u,lenn)) 

        heap = [(0,0)]

        while heap:
            lenn, node = heappop(heap)

            if node not in visited:
                visited.add(node)

                for ni,wh in graph[node]:
                    if dist[ni] > dist[node] + wh and  dist[node] + wh < disappear[ni]:
                        dist[ni] = dist[node] + wh

                        heappush(heap,(dist[ni] , ni))


        # print(dist)
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist

