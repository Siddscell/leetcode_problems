from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            nodes = []
            edge_count = 0

            while stack:
                cur = stack.pop()
                if visited[cur]:
                    continue
                visited[cur] = True
                nodes.append(cur)
                edge_count += len(graph[cur])

                for nei in graph[cur]:
                    if not visited[nei]:
                        stack.append(nei)

            # each undirected edge counted twice
            edge_count //= 2
            size = len(nodes)
            return edge_count == size * (size - 1) // 2

        ans = 0
        for i in range(n):
            if not visited[i]:
                if dfs(i):
                    ans += 1

        return ans