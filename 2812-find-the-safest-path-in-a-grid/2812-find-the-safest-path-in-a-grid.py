from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1:
        # Find the distance of every cell from its nearest thief.
        # Since all thieves are starting points, run a multi-source BFS.
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2:
        # We now need a path where the minimum distance to a thief
        # is as large as possible.
        #
        # Similar to Dijkstra:
        # Instead of minimizing cost, we maximize the minimum value
        # seen along the path.
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while pq:
            # Current path's safeness.
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if visited[x][y]:
                continue
            visited[x][y] = True

            # First time reaching the destination gives the answer,
            # because the priority queue always explores the safest path first.
            if x == n - 1 and y == n - 1:
                return safe

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    # The safeness of the new path is limited by
                    # the weakest cell visited so far.
                    new_safe = min(safe, dist[nx][ny])
                    heapq.heappush(pq, (-new_safe, nx, ny))

        return 0