from bisect import bisect_left,bisect_right
class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mod=10**9+7
        pos=[]
        dig=[]
        prefix=[0]
        h=[0]
        pow10=[1]
        ans=[]
        for i,n in enumerate(s):
            if n!='0':
                pos.append(i)
                dig.append(n)
                prefix.append(prefix[-1]+int(dig[-1]))
                h.append((h[-1]*10+int(dig[-1]))%mod)
                pow10.append((pow10[-1]*10)%mod)
        for a,b in queries:
            l=bisect_left(pos,a)
            r=bisect_right(pos,b)
            if l>=r:
                ans.append(0)
                continue
            ln=r-l
            num=(h[r]-h[l]*pow10[ln])%mod
            suum=prefix[r]-prefix[l]
            
            ans.append((num*suum)%mod)
        return ans