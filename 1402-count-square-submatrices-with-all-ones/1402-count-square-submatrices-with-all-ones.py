class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        def bound(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

        psum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + matrix[i - 1][j - 1]

        def check(i, j, size):
            r2, c2 = i + size - 1, j + size - 1
            if bound(r2, c2):
                square_sum = psum[r2 + 1][c2 + 1] - psum[i][c2 + 1] - psum[r2 + 1][j] + psum[i][j]
                return square_sum == size * size
            return False

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    size = 1
                    while check(i, j, size):
                        ans += 1
                        size += 1

        return ans
