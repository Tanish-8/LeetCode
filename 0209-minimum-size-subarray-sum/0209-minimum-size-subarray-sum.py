class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=n+1
        left=0
        current_sum=0
        for right in range(n):
            current_sum+=nums[right]
            while current_sum>=target:
                ans=min(ans,right-left+1)
                current_sum-=nums[left]
                left+=1
        if ans==n+1:
            return 0
        return ans