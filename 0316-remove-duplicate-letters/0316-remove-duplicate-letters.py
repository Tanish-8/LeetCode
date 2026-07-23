class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        stack.append(s[0])
        n=len(s)
        def dfs(stack,i):
            if i==n:
                return
            if len(stack)==0:
                stack.append(s[i])
                dfs(stack,i+1)
            elif stack[-1]<s[i]:
                if s[i] in stack:
                    dfs(stack,i+1)
                else:
                    stack.append(s[i])
                    dfs(stack,i+1)
            elif stack[-1]==s[i]:
                dfs(stack,i+1)
            else:
                if s[i] in stack:
                    dfs(stack,i+1)
                    return
                elif stack[-1] not in s[i+1:]:
                    stack.append(s[i])
                    dfs(stack,i+1)
                else:
                    stack.pop()
                    dfs(stack,i)
        dfs(stack,1)
        ans=""
        for i in stack:
            ans+=i
        return ans
        