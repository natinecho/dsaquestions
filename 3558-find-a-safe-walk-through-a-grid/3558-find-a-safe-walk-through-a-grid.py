class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def bound(i,j):
            return 0 <= i < len(grid) and  0 <= j < len(grid[i])

        di = [(0,1),(1,0),(-1,0),(0,-1)]
        

        def dikstra(): 
            heap = [(grid[0][0],0,0)]
            visited = set()
            ans = float("inf")
            
            while heap:
                hel,row,col = heappop(heap)

                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    ans = min(ans,hel)

                if (row,col) not in visited:
                    visited.add((row,col))
                    for r,c in di:
                        nr,nc = row + r, col + c
                        
                        if bound(nr,nc) and (nr,nc) not in visited:
                            heappush(heap,(hel + grid[nr][nc],nr,nc))
            
            return ans

        
        return dikstra() < health




        