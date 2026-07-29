class Solution(object):
    def sortColors(self, nums):
        start=0
        mid=0
        end=len(nums)-1
        while mid<=end:
            if nums[mid]==2:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1
            elif nums[mid]==0:
                nums[mid],nums[start]=nums[start],nums[mid]
                start+=1
                mid+=1
            else:
                mid+=1
        return nums