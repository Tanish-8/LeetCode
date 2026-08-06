class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        rows=len(matrix)
        cols=len(matrix[0])
        k=0
        i=0
        j=0
        while True:
            while i==k and j<cols-k:
                ans.append(matrix[i][j])
                j+=1
                if len(ans)==rows*cols:
                    return ans
            if i+1<rows-k:
                i+=1
            j-=1
            while i<rows-k and j==cols-k-1:
                ans.append(matrix[i][j])
                i+=1
                if len(ans)==rows*cols:
                    return ans
            if j-1>=k:
                j-=1
            i-=1
            while i==rows-k-1 and j>=k:
                ans.append(matrix[i][j])
                j-=1
                if len(ans)==rows*cols:
                    return ans
            if i-1>=k+1:
                i-=1
            j+=1
            while i>=k+1 and j==k:
                ans.append(matrix[i][j])
                i-=1
                if len(ans)==rows*cols:
                    return ans
            k+=1
            if j+1<cols-k:
                j+=1
            i+=1