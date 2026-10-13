class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq=[x*x for x in nums]
        s=sorted(sq)
        n=len(s)
        pos=sum(x for x in s[n//2:])
        neg=sum(x for x in s[:n//2])
        return pos-neg
