class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count==0:
                el=nums[i]
                count=1
            else:
                if el==nums[i]:
                    count+=1
                else:
                    count-=1
        return el