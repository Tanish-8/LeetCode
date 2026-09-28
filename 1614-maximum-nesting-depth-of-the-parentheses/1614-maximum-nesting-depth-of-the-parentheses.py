class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        temp=0
        for ch in s:
            if ch=="(":
                temp+=1
                ans=max(ans,temp)
            elif ch==")":
                temp-=1
            else:
                continue
        return ans