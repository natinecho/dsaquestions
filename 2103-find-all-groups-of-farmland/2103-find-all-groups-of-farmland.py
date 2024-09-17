class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        def bound(i,j):
            return 0 <= i < len(land) and 0 <= j < len(land[0])

        di = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):
            st = [(i,j)]
            arr = []

            while st:
                row,col = st.pop()
                arr.append((row,col))

                for r,c in di:
                    nr,nc = row + r ,  col + c

                    if bound(nr,nc) and (nr,nc) not in visited and land[nr][nc] == 1:
                        st.append((nr,nc))
                        visited.add((nr,nc))

            minn = min(arr)
            maxx = max(arr)

            return [minn[0],minn[1],maxx[0],maxx[1]]

        visited = set()
        ans = []

        for i in range(len(land)):
            for j in range(len(land[0])):
                if bound(i,j) and (i,j) not in visited and land[i][j] == 1:
                    visited.add((i,j))
                    ans.append(dfs(i,j))

            
        return ans

