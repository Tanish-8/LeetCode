class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq={}
        for ch in word:
            freq[ch]=freq.get(ch,0)+1
        arr=sorted(freq.values(),reverse=True)
        ans=0
        for i,f in enumerate(arr):
            ans+=(i//8+1)*f
        return ans