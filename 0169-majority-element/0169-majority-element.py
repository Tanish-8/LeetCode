class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key, val in freq.items():
            if val>n/2:
                return key
