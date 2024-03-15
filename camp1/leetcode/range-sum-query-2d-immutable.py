class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.psum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.psum[i][j] = self.psum[i][j-1] + self.psum[i - 1][j] -self.psum[i-1][j-1] + matrix[i][j]


        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.psum[r2][c2] - self.psum[r1 -1][c2] - self.psum[r2][c1 - 1] + self.psum[r1 -1][c1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)