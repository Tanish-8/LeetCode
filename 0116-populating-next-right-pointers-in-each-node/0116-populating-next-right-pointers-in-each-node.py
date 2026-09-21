"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        q=deque([root])
        while q:
            n=len(q)
            for i in range(n):
                node=q[i]
                if i<n-1:
                    node.next=q[i+1]
                else:
                    node.next=None
            for i in range(n):
                node=q.popleft()
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
        return root