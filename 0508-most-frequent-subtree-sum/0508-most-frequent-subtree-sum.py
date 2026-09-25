# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        d=dict()
        def dfs(root,d):
            if root is None:
                return 0
            leftsum=dfs(root.left,d)
            rightsum=dfs(root.right,d)
            s=leftsum+rightsum+root.val
            d[s]=d.get(s,0)+1
            return s
        dfs(root,d)
        h=max(d.values())
        ans=[]
        for a,b in d.items():
            if b==h:
                ans.append(a)
        return ans