# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q=deque([root])
        ans=0
        while q:
            n=len(q)
            lvl=[]
            for i in range(n):
                p=q.popleft()
                lvl.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            s=sorted(lvl)
            pos={v:i for i,v in enumerate(lvl)}
            for i in range(len(lvl)):
                if lvl[i]!=s[i]:
                    j=pos[s[i]]
                    lvl[i], lvl[j]=lvl[j], lvl[i]
                    pos[lvl[i]]=i
                    pos[lvl[j]]=j
                    ans+=1
        return ans       