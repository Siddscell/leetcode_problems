from typing import List
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build the graph.
        # Since the roads are bidirectional, store both directions.
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        # The key idea:
        # We only care about the connected component that contains city 1.
        #
        # Because the problem allows revisiting cities and roads,
        # any road inside this connected component can be part of a path
        # from 1 to n. So the answer is simply the smallest road distance
        # seen anywhere in this component.
        #
        # In other words:
        # - walk through all cities reachable from 1
        # - keep track of the minimum edge weight encountered
        # - return that minimum
        q = deque([1])
        visited = set([1])

        ans = float("inf")

        while q:
            city = q.popleft()

            for nxt, dist in graph[city]:
                # Every edge we see may be the bottleneck of some valid path,
                # so keep the global minimum inside this component.
                ans = min(ans, dist)

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return ans