class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        l=0
        r=len(matrix)-1

        while(l<=r):
            mid=(l+r)//2

            if matrix[mid][-1]==target:
                return True
            elif matrix[mid][-1]<target:
                l=mid+1
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                row=matrix[mid]
                break

        l=0
        r=len(row)-1

        while(l<=r):
            mid=(l+r)//2

            if row[mid]==target:
                return True
            elif row[mid]<target:
                l=mid+1
            else:
                r=mid-1

        return False