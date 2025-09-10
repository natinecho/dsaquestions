class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def hasCycle(node,prev):
            if node in visited:
                return True
            
            visited.add(node)
            for n in graph[node]:
                if n != prev:
                    if hasCycle(n,node):
                        return True
            return False 

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            visited = set()
            if hasCycle(a,-1):
                return [a,b]
        

        return []
