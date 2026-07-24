class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        sum=0
        while n!=0:
            rem=n%10
            if rem!=0:
                x=x*10+rem
                sum+=rem
            n//=10
        x=int(str(x)[::-1])
        return x*sum