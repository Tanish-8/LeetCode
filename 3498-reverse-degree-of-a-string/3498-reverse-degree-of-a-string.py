class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        i=1
        for ch in s:
            ans+=(i*(ord('z')-ord(ch)+1))
            i+=1
        return ans