# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:48 ms,击败了39.57% 的Python3用户 内存消耗:13.9 MB,击败了5.41% 的Python3用户
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         def helper(curr_state):
#             if len(curr_state) == n:
#                 res.append(curr_state)
#
#             for i in nums:
#                 if i not in curr_state:
#                     helper(curr_state + [i])
#         helper([])
#         return res

# 2 解答成功: 执行耗时:44 ms,击败了64.65% 的Python3用户 内存消耗:13.9 MB,击败了5.41% 的Python3用户
# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         def backtrack(first=0):
#             # 所有数都填完了
#             if first == n:
#                 res.append(nums[:])
#             for i in range(first, n):
#                 # 动态维护数组
#                 nums[first], nums[i] = nums[i], nums[first]
#                 # 继续递归填下一个数
#                 backtrack(first + 1)
#                 # 撤销操作
#                 nums[first], nums[i] = nums[i], nums[first]
#
#         n = len(nums)
#         res = []
#         backtrack()
#         return res

# 3 解答成功: 执行耗时:48 ms,击败了39.59% 的Python3用户 内存消耗:13.9 MB,击败了5.41% 的Python3用户
# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         res = []
#         def helper(curr_path, not_used_nums):
#             if len(curr_path) == n:
#                 res.append(curr_path)
#                 return
#             for i in not_used_nums:
#                 new_not_used_nums = not_used_nums.copy()
#                 new_not_used_nums.remove(i)
#                 helper(curr_path+[i], new_not_used_nums)
#         helper([], nums)
#         return res

# 4 解答成功: 执行耗时:44 ms,击败了64.71% 的Python3用户 内存消耗:14 MB,击败了5.41% 的Python3用户
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        used = [False] * n
        def helper(curr_path):
            if len(curr_path) == n:
                res.append(curr_path)
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                helper(curr_path+[nums[i]])
                used[i] = False
        helper([])
        return res

# leetcode submit region end(Prohibit modification and deletion)
