class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ans = []
        q = []
        for b in boxGrid:
            q.clear()
            j = len(boxGrid[0])-1
            while j>=0:
                if b[j]=='.':
                    q.append(j)
                    j-=1
                elif b[j]=='*':
                    q.clear()
                    j-=1
                elif len(q)>0:
                    b[q[0]]='#'
                    q.pop(0)
                    b[j]='.'
                else:
                    j-=1
        print(boxGrid)
        ans = [[boxGrid[j][i] for j in range(len(boxGrid)-1,-1,-1)] for i in range(len(boxGrid[0]))]

        return ans