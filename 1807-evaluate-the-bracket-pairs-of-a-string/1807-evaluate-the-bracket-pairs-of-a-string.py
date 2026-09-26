class Solution(object):
    def evaluate(self, s, knowledge):
        d = {}
        for key, value in knowledge:
            d[key] = value
        ans = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""
                while s[i] != ')':
                    key += s[i]
                    i += 1
                if key in d:
                    ans.append(d[key])
                else:
                    ans.append("?")
                i += 1
            else:
                ans.append(s[i])
                i += 1
        return "".join(ans)