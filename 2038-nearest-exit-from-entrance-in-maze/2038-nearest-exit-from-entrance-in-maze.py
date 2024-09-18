class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([(entrance[0],entrance[1],0)])

        def bound(i,j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0]) 

        di = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set([(entrance[0],entrance[1])])

        while que:
            row,col,count = que.popleft()

            for r,c in di:
                nr,nc = row + r,col + c
                if bound(nr,nc) and (nr,nc) not in visited and maze[nr][nc] == ".":
                    if nr == 0 or nr == (len(maze) - 1) or nc == 0 or nc == (len(maze[0]) - 1):
                        return count + 1
                    else:
                        que.append((nr,nc,count + 1))
                        visited.add((nr,nc))
                
        return -1