class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sumMat = [[0]*(len(self.matrix[0])+1) for _ in range(len(self.matrix)+1)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # BRUTE FORCE
        # res = 0
        # for i in range(row1,row2+1):
        #     for j in range(col1,col2+1):
        #         res += self.matrix[i][j]
        # return res

        # PREFIX BASED SOLUTION
        for i in range(len(self.matrix)):
            prefix = 0
            for j in range(len(self.matrix[0])):
                prefix += self.matrix[i][j]
                above = self.sumMat[i][j+1]
                self.sumMat[i+1][j+1] = prefix + above

        return self.sumMat[row2+1][col2+1]-self.sumMat[row1][col2+1] - self.sumMat[row2+1][col1] + self.sumMat[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)