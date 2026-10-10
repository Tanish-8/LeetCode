# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        def maxHP(root,parent,value,height):
            if root is None:
                return None, -1
            if root.val==value:
                return parent, height
            left=maxHP(root.left, root.val, value, height+1)
            if left[1]!=-1:
                return left
            return maxHP(root.right, root.val, value, height+1)
        parent_x, height_x=maxHP(root, None, x, 0)
        parent_y, height_y=maxHP(root, None, y, 0)
        return parent_x!=parent_y and height_x==height_y