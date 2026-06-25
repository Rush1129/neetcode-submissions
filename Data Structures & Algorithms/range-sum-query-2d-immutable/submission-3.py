class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.presum = matrix

        for i in range(len(matrix)):
            rowc=0
            for j in range(len(matrix[i])):
                if i==0 and j>0:
                    self.presum[i][j] += self.presum[i][j-1]
                elif i>0 and j==0:
                    rowc+=matrix[i][j]
                    self.presum[i][j] += self.presum[i-1][j]
                elif i>0 and j>0:
                    rowc+=matrix[i][j]
                    self.presum[i][j] = (rowc+self.presum[i-1][j])
        self.presum.insert(0,[0]*len(matrix[0]))
        for i in self.presum:
            i.insert(0,0)
        # print(self.presum)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        # print(row1,col1,row2,col2)
        return (self.presum[row2][col2]-(self.presum[row1-1][col2]+self.presum[row2][col1-1]) + self.presum[row1-1][col1-1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)