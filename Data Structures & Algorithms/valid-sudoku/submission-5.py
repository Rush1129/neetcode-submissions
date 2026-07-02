class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s,s1,s2,s3,s4 = set(),set(),set(),set(),set()
        for i in range(0, len(board)):
            s.clear()
            s1.clear()
            for j in range(0, len(board[i])):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if num in s:
                        return False
                    s.add(num)

                    if(j<3):
                        if(num in s2):
                            return False
                        s2.add(num)
                    elif(j<6):
                        if(num in s3):
                            return False
                        s3.add(num)
                    else:
                        if(num in s4):
                            return False
                        s4.add(num)

                if board[j][i]!='.': 
                    num = int(board[j][i])
                    if num in s1:
                        return False
                    print(num) 
                    s1.add(num)

            if (i+1)%3==0:
                s2.clear()
                s3.clear()
                s4.clear()
                
        return True