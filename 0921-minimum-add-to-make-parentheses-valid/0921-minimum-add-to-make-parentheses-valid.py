class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=0
        s2=0
        for i in range(len(s)):
            if s[i]=="(":
                s1+=1
            else:
                if s1>0:
                    s1-=1
                else:
                    s2+=1
        return s1+s2

            