from collections import deque
from typing import List
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        dp = [[0] * 26 for _ in range(n)]
        visited = 0
        max_color = 0
        while q:
            u = q.popleft()
            visited += 1
            color = ord(colors[u]) - ord('a')
            dp[u][color] += 1
            max_color = max(max_color, dp[u][color])
            for v in adj[u]:
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c])
                
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if visited != n:
            return -1
        
        return max_color