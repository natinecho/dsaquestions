class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bound(r,c):
            return 0<= r< len(board) and 0<= c < len(board[0])

        di = [(0,1),(1,0),(0,-1),(-1,0)]

        def back(path,row,col,visited):
            if len(path) == len(word):
                return True

            ans = False

            for r,c in di:
                n_row = row + r
                n_col = col + c

                if bound(n_row,n_col) and board[n_row][n_col] == word[len(path)] and (n_row,n_col) not in visited:
                    path.append(board[n_row][n_col])
                    visited.add((n_row,n_col))

                    if back(path,n_row,n_col,visited):
                        return True

                    path.pop()
                    visited.remove((n_row,n_col))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                path = []
                visited = set()

                if board[i][j] == word[len(path)]:
                    path.append(board[i][j])
                    visited.add((i,j))

                    if back(path,i,j,visited):
                        return True

                    path.pop()
                    visited.remove((i,j))

        return False





                    





        