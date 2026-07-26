class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        n=sorted(n)
        return int(n[-1])*int(n[-2])