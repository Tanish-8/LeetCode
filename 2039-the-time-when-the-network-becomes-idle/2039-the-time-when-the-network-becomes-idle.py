class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        n=len(patience)
        graph=[[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist=[-1]*n
        dist[0]=0
        q=deque([0])
        while q:
            g=q.popleft()
            for neighbor in graph[g]:
                if dist[neighbor]==-1:
                    dist[neighbor]=dist[g]+1
                    q.append(neighbor)
        ans=0
        for i in range(1,n):
            round_trip=2*dist[i]
            last_msg=((round_trip-1)//patience[i])*patience[i]
            total_time=round_trip+last_msg+1
            ans=max(ans,total_time)
        return ans