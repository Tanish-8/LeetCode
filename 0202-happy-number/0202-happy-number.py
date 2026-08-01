class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        def dfs(n):
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
            s=0
            for ch in str(n):
                i=int(ch)
                s+=i*i
            return dfs(s)
        return dfs(n)