class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        ans=-float('inf')
        ans=max(ans,nums[-1]*nums[-2]*nums[-3])
        ans=max(ans,nums[1]*nums[2]*nums[0])
        ans=max(ans,nums[1]*nums[-1]*nums[0])
        ans=max(ans,nums[-2]*nums[-1]*nums[0])
        return ans