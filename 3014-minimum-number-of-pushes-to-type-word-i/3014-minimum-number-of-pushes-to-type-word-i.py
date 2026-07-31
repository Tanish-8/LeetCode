class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        div=n//8
        rem=n%8
        print(n,div,rem)
        ans=0
        for i in range(1,div+1):
            ans+=8*i
        ans+=rem*(div+1)
        return ans