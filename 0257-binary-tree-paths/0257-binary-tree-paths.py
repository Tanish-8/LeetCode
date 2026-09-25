# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans=[]
        def dfs(root,st):
            if root is None:
                return       
            st+=str(root.val)
            if root.left is None and root.right is None:
                ans.append(st)
                return
            if root.left:
                dfs(root.left,st+"->")
            if root.right:
                dfs(root.right,st+"->")
        dfs(root,"")
        return ans