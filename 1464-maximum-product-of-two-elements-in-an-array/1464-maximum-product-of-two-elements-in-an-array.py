class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        b=0
        for i in range(1,len(nums)):
            if nums[i]>=a:
                a,b=nums[i],a
            elif nums[i]<a and nums[i]>b:
                b=nums[i]
            else:
                continue
        return (a-1)*(b-1)
