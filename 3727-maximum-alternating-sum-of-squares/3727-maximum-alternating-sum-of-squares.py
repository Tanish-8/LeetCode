class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq=[x*x for x in nums]
        s=sorted(sq)[::-1]
        n=len(s)
        print(s)
        return sum(s[i] for i in range((n+1)//2))-sum(s[i] for i in range((n+1)//2,n))
