class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        di = [(0,1),(1,0),(-1,0),(0,-1)]

        def bound (i , j ):
            return 0 <= i < len(image) and 0 <= j < len(image[0])

        que = deque([(sr,sc)])
        visited = set([(sr,sc)])

        coll = image[sr][sc]
        image[sr][sc] = color

        while que:
            row , col = que.popleft()

            for r,c in di:
                nr = row + r 
                nc = col + c 

                if bound(nr,nc) and image[nr][nc] == coll and (nr,nc) not in visited:
                    image[nr][nc] = color
                    que.append((nr,nc))
                    visited.add((nr,nc))

        return image


        