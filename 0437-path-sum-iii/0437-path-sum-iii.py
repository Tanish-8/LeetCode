# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix=defaultdict(int)
        prefix[0]=1
        ans=[0]
        def dfs(root,cs):
            if not root:
                return 
            cs+=root.val
            ans[0]+=prefix[cs-targetSum]
            prefix[cs]+=1
            dfs(root.left,cs)
            dfs(root.right,cs)
            prefix[cs]-=1
            return 
        dfs(root,0)
        return ans[0]