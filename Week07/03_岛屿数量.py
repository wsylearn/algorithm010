# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:92 ms,击败了42.35% 的Python3用户 内存消耗:14.5 MB,击败了6.67% 的Python3用户
# DFS
# O(m*n),O(m*n)
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         m = len(grid)
#         n = len(grid[0])
#
#         def dfs(i,j):
#             if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
#                 return
#             grid[i][j] = "0"
#             dfs(i-1, j)
#             dfs(i, j-1)
#             dfs(i, j+1)
#             dfs(i+1, j)
#
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     res += 1
#                     dfs(i, j)
#         return res

# 2 解答成功: 执行耗时:76 ms,击败了82.13% 的Python3用户 内存消耗:14.1 MB,击败了6.67% 的Python3用户
# BFS
# O(m*n),O(min(m,n))

# import collections
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         m = len(grid)
#         n = len(grid[0])
#
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     res += 1
#                     grid[i][j] = "0"
#                     neighbors = collections.deque([(i, j)])
#                     while neighbors:
#                         x, y = neighbors.popleft()
#                         for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                             if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
#                                 neighbors.append((new_x, new_y))
#                                 grid[new_x][new_y] = "0"
#
#         return res

# # 3
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         m, n = len(grid), len(grid[0])
#         p = [[None]*n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 p[i][j] = (i, j)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     self._union(p, i, j)
#
#     def _union(self, p, i, j):
#         p = self._parent(p, i, j)
#         p[i][j] = p
#
#     def _parent(self, p, i, j):
#         root = (i, j)
#         while p[root[0][root[1]] != root:
#             root = p[root[0][root[1]]
#         return root


# leetcode submit region end(Prohibit modification and deletion)
