# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
#  示例:
#
#  X X X X
# X O O X
# X X O X
# X O X X
#
#
#  运行你的函数后，矩阵变为：
#
#  X X X X
# X X X X
# X X X X
# X O X X
#
#
#  解释:
#
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:52 ms,击败了81.88% 的Python3用户 内存消耗:15.1 MB,击败了7.69% 的Python3用户
# dfs
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#         m, n = len(board), len(board[0])
#
#         def dfs(i, j):
#             board[i][j] = "#"
#             for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#                 new_i, new_j = i + di, j + dj
#                 if 1 <= new_i < m and 1 <= new_j < n and board[new_i][new_j] == "O":
#                     dfs(new_i, new_j)
#
#         for i in range(m):
#             if board[i][0] == "O":
#                 dfs(i, 0) # 第一列
#             if board[i][n-1] == "O":
#                 dfs(i, n-1) # 最后一列
#
#         for j in range(n):
#             if board[0][j] == "O":
#                 dfs(0, j) # 第一行
#             if board[m-1][j] == "O":
#                 dfs(m-1, j) # 最后一行
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 if board[i][j] == "#":
#                     board[i][j] = "O"

# 2 解答成功: 执行耗时:56 ms,击败了66.11% 的Python3用户 内存消耗:14.4 MB,击败了30.77% 的Python3用户
# BFS
# from collections import deque
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#         m, n = len(board), len(board[0])
#         def bfs(i, j):
#             queue = deque()
#             queue.append((i, j))
#             while queue:
#                 i, j = queue.popleft()
#                 if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
#                     board[i][j] = "#"
#                     for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#                         queue.append((i + di, j + dj))
#
#         for i in range(m):
#             if board[i][0] == "O":
#                 bfs(i, 0) # 第一列
#             if board[i][n-1] == "O":
#                 bfs(i, n-1) # 最后一列
#
#         for j in range(n):
#             if board[0][j] == "O":
#                 bfs(0, j) # 第一行
#             if board[m-1][j] == "O":
#                 bfs(m-1, j) # 最后一行
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 if board[i][j] == "#":
#                     board[i][j] = "O"

# 3 解答成功: 执行耗时:328 ms,击败了6.64% 的Python3用户 内存消耗:17.7 MB,击败了7.69% 的Python3用户
# 并查集
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"



# leetcode submit region end(Prohibit modification and deletion)
