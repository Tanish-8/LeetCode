class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                a=i
                break
        if a==-1:
            nums.reverse()
            return
        for i in range(len(nums)-1,a,-1):
            if nums[i]>nums[a]:
                nums[i],nums[a]=nums[a],nums[i]
                break
        nums[a+1:]=nums[a+1:][::-1]
        return
        