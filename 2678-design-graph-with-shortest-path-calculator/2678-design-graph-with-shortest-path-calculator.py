class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.N = n

        for u,v,w in edges:
            self.graph[u].append((v,w))
         

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1],edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")] * (self.N)
        dist[node1] = 0

        heap = [(0,node1)]
        visited = set()

        while heap:
            wh,node = heappop(heap)

            if node == node2:
                return dist[node2]

            if node not in visited:
                visited.add(node)
                for ni, w in self.graph[node]:
                    if dist[ni] > dist[node] + w:
                        dist[ni] =  dist[node] + w
                        heappush(heap,(dist[ni],ni))

        return  -1 

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)