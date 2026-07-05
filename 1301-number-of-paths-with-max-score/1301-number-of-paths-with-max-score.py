class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        best = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        best[0][0] = 0
        ways[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue

                if i == 0 and j == 0:
                    continue

                mx = -1
                cnt = 0

                for x, y in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if x < 0 or y < 0:
                        continue
                    if best[x][y] == -1:
                        continue

                    if best[x][y] > mx:
                        mx = best[x][y]
                        cnt = ways[x][y]
                    elif best[x][y] == mx:
                        cnt = (cnt + ways[x][y]) % MOD

                if mx == -1:
                    continue

                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])

                best[i][j] = mx + val
                ways[i][j] = cnt

        if ways[n - 1][n - 1] == 0:
            return [0, 0]

        return [best[n - 1][n - 1], ways[n - 1][n - 1]]