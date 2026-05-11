class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for i in board:
            s.clear()
            for j in i:
                if(j=='.'):
                    continue
                if j in s:
                    return False
                s.add(j)
        s.clear()
        
        for i in range(len(board[0])):
            s.clear()
            for j in range(len(board)):
                n = board[j][i]
                if(n=='.'):
                    continue
                intn = int(n)
                if intn in s:
                    return False
                s.add(intn)
        s.clear()

        for sq in range(9):
            s.clear()
            for i in range(3):
                for j in range(3):
                    r = (sq//3)*3 + i
                    c = (sq%3)*3 + j

                    if(board[r][c] == '.'):
                        continue
                    if(board[r][c] in s):
                        return False
                    s.add(board[r][c])
         
        return True