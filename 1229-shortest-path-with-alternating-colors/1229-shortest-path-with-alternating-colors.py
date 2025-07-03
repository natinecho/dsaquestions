
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
     
        rg = defaultdict(list)
        bg = defaultdict(list)

        for u, v in redEdges:
            rg[u].append(v)
        for u, v in blueEdges:
            bg[u].append(v)

        answer = [-1] * n
        visited = set()
        que = deque()

       
        que.append((0, 0, -1))  
        visited.add((0, -1))

        while que:
            node, length, last_color = que.popleft()

            if answer[node] == -1:
                answer[node] = length
            else:
                answer[node] = min(answer[node], length)

            if last_color != 0:  
                for nei in rg[node]:
                    if (nei, 0) not in visited:
                        visited.add((nei, 0))
                        que.append((nei, length + 1, 0))

            if last_color != 1: 
                for nei in bg[node]:
                    if (nei, 1) not in visited:
                        visited.add((nei, 1))
                        que.append((nei, length + 1, 1))

        return answer
