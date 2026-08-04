class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        s=set(nums)
        ans=1
        for i in s:
            if i-1 not in s:
                x=i
                cnt=1
                while i+1 in s:
                    i+=1
                    cnt+=1
                ans=max(ans,cnt)
        return ans