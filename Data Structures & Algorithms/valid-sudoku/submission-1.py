class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in range(0, len(board)):
            s.clear()
            for j in range(0, len(board[i])):
                if board[i][j] == '.':
                    continue
                
                num = int(board[i][j])
                if num in s:
                    return False
                
                s.add(num)

        for i in range(0, len(board[0])):
            s.clear()
            for j in range(0, len(board)):
                if board[j][i] == '.':
                    continue
                
                num = int(board[j][i])
                if num in s:
                    return False
                
                s.add(num)

        s.clear()       
        s1, s2 = set(), set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j]=='.'):
                    continue
                num = int(board[i][j])

                if(j<3):
                    if(num in s):
                        return False
                    s.add(num)
                elif(j<6):
                    if(num in s1):
                        return False
                    s1.add(num)
                else:
                    if(num in s2):
                        return False
                    s2.add(num)

            if (i+1)%3==0:
                s.clear()
                s1.clear()
                s2.clear()

        return True