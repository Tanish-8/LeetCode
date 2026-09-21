# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque()
        ans=[]
        q.append(root)
        lvl=0
        while q:
            a=[]
            n=len(q)
            for i in range(n):
                r=q.popleft()
                if r.left!=None:
                    q.append(r.left)
                if r.right!=None:
                    q.append(r.right)
                a.append(r.val)
            if lvl%2==0:
                ans.append(a)
            else:
                ans.append(a[::-1])
            lvl+=1
        return ans