class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        sum=0
        for s in str(n):
            if s!='0':
                i=int(s)
                x=x*10+i
                sum+=i
        return x*sum