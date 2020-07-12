# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  判断你是否能够到达最后一个位置。
#
#  示例 1:
#
#  输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
#  示例 2:
#
#  输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#  Related Topics 贪心算法 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# 暴力搜索， 指数级时间复杂度

# class Solution:
#     def canJump(self, nums) -> bool:
#         n = len(nums)
#         self.flag = False
#
#         def helper(index):
#             if index >= n:
#                 return
#             if index == n - 1:
#                 self.flag = True
#                 return
#             for i in range(1, nums[index] + 1):
#                 if self.flag:
#                     return
#                 helper(index + i)
#
#         helper(0)
#         return self.flag

# 2 运行失败: Time Limit Exceeded stdout: null
# 类似斐波那契数列一样
# O（n^2）
# class Solution:
#     def canJump(self, nums) -> bool:
#         n = len(nums)
#         flag = [True] + [False] * (n-1)
#         for i in range(n):
#             if flag[i]:
#                 num = nums[i]
#                 for j in range(1, num+1):
#                     if i+j < n:
#                         flag[i+j] = True
#         return flag[-1]

# 3 解答成功: 执行耗时:40 ms,击败了97.72% 的Python3用户 内存消耗:15 MB,击败了6.90% 的Python3用户
# 从后往前贪心
# O(n), O(1)
# class Solution:
#     def canJump(self, nums) -> bool:
#         if not nums:
#             return False
#         end_reachable_index = len(nums) - 1
#         for i in range(end_reachable_index, -1, -1):
#             if (i + nums[i]) >= end_reachable_index:
#                 end_reachable_index = i
#         return end_reachable_index == 0

# 4 解答成功: 执行耗时:52 ms,击败了70.95% 的Python3用户 内存消耗:15.1 MB,击败了6.90% 的Python3用户
# O(n), O(1)
# class Solution:
#     def canJump(self, nums) -> bool:
#         reach = 0
#         n = len(nums)
#         for i in range(n):
#             if i > reach:
#                 return False
#             reach = max(reach, i+nums[i])
#         return True

# class Solution:
#     def canJump(self, nums) :
#         max_i = 0       #初始化当前能到达最远的位置
#         for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
#             if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
#                 max_i = i+jump  #更新最远能到达位置
#         return max_i>=i



# 5 解答成功: 执行耗时:48 ms,击败了84.65% 的Python3用户 内存消耗:15.1 MB,击败了6.90% 的Python3用户
# O(n), O(1)
# class Solution:
#     def canJump(self, nums) -> bool:
#         reach = 0
#         n = len(nums)
#         i = 0
#         while i <= reach and reach < n-1:
#             reach = max(reach, i+nums[i])
#             i += 1
#         return reach >= n-1

# 6 解答成功: 执行耗时:52 ms,击败了70.95% 的Python3用户 内存消耗:15 MB,击败了6.90% 的Python3用户
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums: return True  # 如果没有0则一定可以到达
        if len(nums) < 2: return True
        max_distance = nums[0]  # 设定可以达到的最大坐标
        for i in range(1, len(nums) - 1):
            if i <= max_distance:  # 表示当前坐标可以达到
                max_distance = max(max_distance, i + nums[i])  # 更新可以达到的最远坐标
            else:
                break
        return max_distance >= len(nums) - 1


# leetcode submit region end(Prohibit modification and deletion)
