class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            b=target-nums[i]
            n=nums[:i]+nums[i+1:]
            if b in n:
                j=n.index(b)
                if j<i:
                    return [i,j]
                else:
                    return [i,j+1]
            else:
                continue
        
        