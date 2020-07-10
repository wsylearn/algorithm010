# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
#  示例:
#
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def helper(curr_state):
#             if len(curr_state) == k:
#                 curr_state.sort()
#                 if curr_state not in res:
#                     res.append(curr_state)
#             for i in range(1, n+1):
#                 if i not in curr_state:
#                     helper(curr_state+[i])
#         helper([])
#         return res
#
# 2 解答成功: 执行耗时:500 ms,击败了56.59% 的Python3用户 内存消耗:15.1 MB,击败了10.53% 的Python3用户
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def helper(start_n, curr_state):
#             if len(curr_state) == k:
#                     res.append(curr_state)
#             for i in range(start_n, n+1):
#                 helper(i+1, curr_state+[i])
#         helper(1, [])
#         return res

# 3 解答成功: 执行耗时:28 ms,击败了99.97% 的Python3用户 内存消耗:15 MB,击败了10.53% 的Python3用户
# import itertools
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return list(itertools.combinations(range(1,n+1),k))


# leetcode submit region end(Prohibit modification and deletion)
