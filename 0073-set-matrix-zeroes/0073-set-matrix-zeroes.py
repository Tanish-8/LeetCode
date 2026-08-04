class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        f_row=False
        f_col=False
        for r in range(m):
            if matrix[r][0]==0:
                f_col=True
                break
        for c in range(n):
            if matrix[0][c]==0:
                f_row=True
                break
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        if f_row:
            for c in range(n):
                matrix[0][c]=0
        if f_col:
            for r in range(m):
                matrix[r][0]=0