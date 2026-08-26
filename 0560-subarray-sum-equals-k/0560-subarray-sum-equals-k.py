class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        prefix_sum=0
        vis={0:1}
        for n in nums:
            prefix_sum+=n
            if prefix_sum-k in vis:
                ans+=vis[prefix_sum-k]
            vis[prefix_sum]=vis.get(prefix_sum,0)+1
        return ans