# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#  示例:
#
#  输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:100 ms,击败了59.05% 的Python3用户 内存消耗:14.4 MB,击败了14.29% 的Python3用户 b
# DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side**2
# leetcode submit region end(Prohibit modification and deletion)
