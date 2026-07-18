class Solution(object):
    def maximumValue(self, n, s, m):
        """
        :type n: int
        :type s: int
        :type m: int
        :rtype: int
        """
        if n==1:
            return s
        return s+m*(n//2)-((n//2)-1)