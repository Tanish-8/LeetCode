class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        asc=sorted(set(arr))
        rank={}
        for i in range(len(asc)):
            rank[asc[i]]=i+1
        return [rank[i] for i in arr]
