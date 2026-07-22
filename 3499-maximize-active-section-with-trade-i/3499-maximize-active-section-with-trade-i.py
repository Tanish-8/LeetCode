class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ones=0
        cnt=s.count('1')
        ans=0
        fz=-1
        z=-1
        for i in range(n):
            if s[i]=="0":
                if fz<0:
                    fz=i
                elif ones>0:
                    if s[i-1]=="1":
                        z=i
                    if i+1==n or s[i+1]=="1":
                        sz=i
                        ans=max(ans,cnt+sz-fz+1-ones)
                        fz=z
                        ones=0
                        z=-1
            else:
                if fz>=0:
                    ones+=1
        if ans==0:
            return cnt
        return ans