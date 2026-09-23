class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total=sum(nums)
        y=total-x
        if y<0:
            return -1
        n=len(nums)
        prefix_sum=[0]*(n+1)
        left=0
        current_sum=0
        ans=0
        for right in range(n):
            current_sum+=nums[right]
            while current_sum>y:
                current_sum-=nums[left]
                left+=1
            if current_sum==y:
                ans=max(ans,right-left+1)
        if ans==0 and y!=0:
            return -1
        return n-ans