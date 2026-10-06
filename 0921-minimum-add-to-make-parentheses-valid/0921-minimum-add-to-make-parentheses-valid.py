class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[s[0]]
        for i in range(1,len(s)):
            ch=s[i]
            if ch=="(":
                stack.append(ch)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)

            