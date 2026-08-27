class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1=0
        count2=0
        el1=float('inf')
        el2=float('inf')
        for n in nums:
            if count1==0 and el2!=n:
                count1=1
                el1=n
            elif count2==0 and el1!=n:
                count2=1
                el2=n
            elif n==el1:
                count1+=1
            elif n==el2:
                count2+=1
            else:
                count1-=1
                count2-=1
        ans=[]
        count1=0
        count2=0
        for n in nums:
            if el1==n:
                count1+=1
            elif el2==n:
                count2+=1
        if count1>len(nums)//3:
            ans.append(el1)
        if count2>len(nums)//3:
            ans.append(el2)
        return ans