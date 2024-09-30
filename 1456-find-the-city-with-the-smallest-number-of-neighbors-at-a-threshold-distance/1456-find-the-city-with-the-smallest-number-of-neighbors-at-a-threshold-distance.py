class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        ans = defaultdict(int)

        for u,v,w in edges:
            graph[u].append((v,w)) 
            graph[v].append((u,w)) 
        
        def find(root):

            que = [(0,root)]
            visited =set()
            while que:
                level,node = heappop(que)

                if level > distanceThreshold:
                    continue

                if node not in visited:
                    ans[root] += 1

                visited.add(node)

                for ni,wh in graph[node]:
                    if ni not in visited:
                        heappush(que,(level + wh,ni))

        for i in range(n):
            find(i)

        minn = min(ans.values())

        maxx = -inf

        for i in ans.keys():
            if ans[i] == minn:
                maxx = max(maxx,i)


        return maxx

