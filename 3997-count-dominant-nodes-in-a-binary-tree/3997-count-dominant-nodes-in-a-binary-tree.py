# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countDominantNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(root):
            if root is None:
                return 0, 0
            left_max, left_count=rec(root.left)
            right_max, right_count=rec(root.right)
            subtree_max=max(root.val, left_max, right_max)
            count=left_count+right_count
            if root.val==subtree_max:
                count+=1
            return subtree_max, count
        m, c=rec(root)
        return c