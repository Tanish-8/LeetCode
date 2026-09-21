"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q=deque()
        ans=[]
        q.append(root)
        while q:
            a=[]
            n=len(q)
            for i in range(n):
                r=q.popleft()
                for child in r.children:
                    if child!=None:
                        q.append(child)
                a.append(r.val)
            ans.append(a)
        return ans