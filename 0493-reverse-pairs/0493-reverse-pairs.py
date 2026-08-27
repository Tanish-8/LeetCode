class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divide(low,high):
            count=0
            mid=(low+high)//2
            if low>=high:
                return 0
            count+=divide(low,mid)
            count+=divide(mid+1,high)
            count+=merge(low,mid,high)
            return count
        def merge(low,mid,high):
            count=0
            right=mid+1
            for left in range(low,mid+1):
                while right<=high and nums[left]>2*nums[right]:
                    right+=1
                count+=right-(mid+1)
            left=low
            right=mid+1
            temp=[]          
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
            nums[low:high+1]=temp
            return count
        return divide(0,len(nums)-1)