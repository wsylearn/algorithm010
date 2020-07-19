# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#  示例:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# 暴力
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         self.min_path = float("inf")
#         def helper(i,j, curr_path):
#             if i >= rows or j >= cols:
#                 return
#             curr_path += grid[i][j]
#             if i == rows - 1 and j == cols - 1:
#                self.min_path = min(self.min_path, curr_path)
#                return
#             helper(i+1, j, curr_path)
#             helper(i, j+1, curr_path)
#         helper(0, 0, 0)
#         return self.min_path

# 2 运行失败: Time Limit Exceeded stdout: null
# 暴力
# O(2^(m+n)), O(m+n)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         def helper(i,j):
#             if i >= rows or j >= cols:
#                 return float("inf")
#             if i == rows - 1 and j == cols - 1:
#                return grid[i][j]
#             return grid[i][j] + min(helper(i+1, j), helper(i, j+1))
#         return helper(0, 0)

# 3
# 二维动态规划
# 3.1 解答成功: 执行耗时:96 ms,击败了5.85% 的Python3用户 内存消耗:15 MB,击败了8.33% 的Python3用户
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[0]*cols for _ in range(rows)]
#         def helper(i, j):
#             if i == rows-1 and j == cols:
#                 return 0
#             elif i == rows and j == cols-1:
#                 return 0
#             elif i >= rows:
#                 return float("inf")
#             elif j >= cols:
#                 return float("inf")
#             else:
#                 return dp[i][j]
#         for i in range(rows-1, -1, -1):
#             for j in range(cols-1, -1, -1):
#                 dp[i][j] = grid[i][j] + min(helper(i+1, j), helper(i, j+1))
#         return dp[0][0]

# 3.2 解答成功: 执行耗时:84 ms,击败了11.33% 的Python3用户 内存消耗:15.1 MB,击败了8.33% 的Python3用户l
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[0]*cols for _ in range(rows)]
#         for i in range(-1,-cols-1, -1):
#             dp[-1][i] = sum(grid[-1][i:])
#         for i in range(-2, -rows-1, -1):
#             for j in range(-1, -cols-1, -1):
#                 if j == -1:
#                     dp[i][j] = grid[i][j] + dp[i+1][j]
#                 else:
#                     dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
#         return dp[0][0]

# 3.3 解答成功: 执行耗时:76 ms,击败了17.98% 的Python3用户 内存消耗:15 MB,击败了8.33% 的Python3用户
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[0]*cols for _ in range(rows)]
#         for i in range(-1, -rows-1, -1):
#             for j in range(-1, -cols-1, -1):
#                 if i == -1:
#                     if j == -1:
#                         dp[i][j] = grid[i][j]
#                     else:
#                         dp[i][j] = grid[i][j] + dp[i][j+1]
#                 else:
#                     if j == -1:
#                         dp[i][j] = grid[i][j] + dp[i+1][j]
#                     else:
#                         dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
#         return dp[0][0]

# 3.4 解答成功: 执行耗时:68 ms,击败了31.12% 的Python3用户 内存消耗:15.2 MB,击败了8.33% 的Python3用户
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[0]*cols for _ in range(rows)]
#         for i in range(-1, -rows-1, -1):
#             for j in range(-1, -cols-1, -1):
#                 if i == -1:
#                     if j == -1:
#                         dp[i][j] = grid[i][j]
#                     else:
#                         dp[i][j] = grid[i][j] + dp[i][j+1]
#                 else:
#                     if j == -1:
#                         dp[i][j] = grid[i][j] + dp[i+1][j]
#                     else:
#                         dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
#         return dp[0][0]

# 3.5 解答成功: 执行耗时:60 ms,击败了66.02% 的Python3用户 内存消耗:15.3 MB,击败了8.33% 的Python3用户
# O(mn),O(mn)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[0]*cols for _ in range(rows)]
#         for i in range(rows):
#             for j in range(cols):
#                 if i == 0:
#                     if j == 0:
#                         dp[i][j] = grid[-i + rows - 1][-j + cols -1]
#                     else:
#                         dp[i][j] = grid[-i + rows - 1][-j + cols -1] + dp[i][j-1]
#                 else:
#                     if j == 0:
#                         dp[i][j] = grid[-i + rows - 1][-j + cols -1] + dp[i-1][j]
#                     else:
#                         dp[i][j] = grid[-i + rows - 1][-j + cols -1] + min(dp[i-1][j], dp[i][j-1])
#         return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
