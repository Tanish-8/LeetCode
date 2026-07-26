class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        msum=nums[0]
        csum=max(0,nums[0])
        for i in range(1,len(nums)):
            csum=max(nums[i],csum+nums[i])
            msum=max(msum,csum)
        return msum