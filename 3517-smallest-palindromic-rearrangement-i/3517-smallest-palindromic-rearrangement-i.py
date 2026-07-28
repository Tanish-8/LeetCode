class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        freq={}
        for i in range(n//2):
            freq[s[i]]=freq.get(s[i],0)+1
        ans=""
        for k,v in sorted(freq.items()):
            ans+=k*v
        if n%2!=0:
            return ans+s[n//2]+ans[::-1]
        return ans+ans[::-1]