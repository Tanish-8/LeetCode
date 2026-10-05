class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        for ch in s:
            if ch=="(":
                stack.append(0)
            else:
                last=stack.pop()
                if last==0:
                    score=1
                else:
                    score=2*last
                stack[-1]+=score
        return stack[0]