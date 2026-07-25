class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=""
        y=""
        s=0
        n=str(n)
        i,j=0,len(n)-1
        while i<=j:
            if i==j:
                if n[i]!='0':
                    x+=n[i]
                    s+=int(n[i])
                break
            if n[i]!='0':
                x+=n[i]
                s+=int(n[i])
            if n[j]!='0':
                y+=n[j]
                s+=int(n[j])
            i+=1
            j-=1
        if not x and not y:
            return 0
        return int(x+y[::-1])*s