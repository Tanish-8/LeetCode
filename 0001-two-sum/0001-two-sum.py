class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vis={}
        for idx,num1 in enumerate(nums):
            num2=target-num1
            if num2 in vis:
                return [idx,vis[num2]]
            vis[num1]=idx
        