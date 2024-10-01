class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []

        def back(node,path):
            if node == len(graph) - 1:
                ans.append(path[::])
                return 

            for ni in graph[node]:
                path.append(ni)
                back(ni,path)
                path.pop()

            return

        back(0,[0])

        return ans
        

            
