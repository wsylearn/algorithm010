# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
#  示例:
#
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:1108 ms,击败了17.90% 的Python3用户 内存消耗:13.9 MB,击败了9.09% 的Python3用户
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#
#         def helper(curr_path, not_used_path):
#             if len(curr_path) == n:
#                 if curr_path not in res:
#                     res.append(curr_path)
#                     return
#             for i in not_used_path:
#                 new_not_used_path = not_used_path.copy()
#                 new_not_used_path.remove(i)
#                 helper(curr_path + [i], new_not_used_path)
#
#         helper([], nums)
#         return res

# 2 解答成功: 执行耗时:1304 ms,击败了8.41% 的Python3用户 内存消耗:14 MB,击败了9.09% 的Python3用户
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         used = [False] * n
#
#         def helper(curr_path):
#             if len(curr_path) == n:
#                 if curr_path not in res:
#                     res.append(curr_path)
#                     return
#             for i in range(n):
#                 if used[i]:
#                     continue
#                 used[i] = True
#                 helper(curr_path + [nums[i]])
#                 used[i] = False
#         helper([])
#         return res
#3 (推荐)解答成功: 执行耗时:48 ms,击败了83.87% 的Python3用户 内存消耗:14.1 MB,击败了9.09% 的Python3用户
# 本题在46题中的剪枝条件是用过的元素不能再使用之外，又添加了一个新的剪枝条件，
# 也就是我们考虑重复部分思考的结果，于是新加的剪枝条件为：
# 当前元素和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过的时候，我们要剪枝！
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         n = len(nums)
#         used = [False] * n
#
#         def helper(curr_path):
#             if len(curr_path) == n:
#                 res.append(curr_path)
#                 return
#             for i in range(n):
#                 if used[i]:
#                     continue
#                 if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
#                     continue
#                 used[i] = True
#                 helper(curr_path + [nums[i]])
#                 used[i] = False
#         helper([])
#         return res

# 4.1 解答成功: 执行耗时:44 ms,击败了93.28% 的Python3用户 内存消耗:14.1 MB,击败了9.09% 的Python3用户
# from collections import Counter
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         counter = Counter(nums)
#         res = []
#         n = len(nums)
#         def helper(counter, curr_path):
#             if len(curr_path) == n:
#                 res.append(curr_path[:])
#
#             for i in counter.keys():
#                 if counter[i] == 0:
#                     continue
#                 counter[i] -= 1
#                 # curr_path.append(i)
#                 helper(counter, curr_path+[i])
#                 # curr_path.pop()
#                 counter[i] += 1
#
#         helper(counter,[])
#         return res

# 4.2
# from collections import Counter
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         counter = Counter(nums)
#         res = []
#         n = len(nums)
#         def helper(curr_path):
#             if len(curr_path) == n:
#                 res.append(curr_path[:])
#
#             for i in counter.keys():
#                 if counter[i] == 0:
#                     continue
#                 counter[i] -= 1
#                 # curr_path.append(i)
#                 helper(curr_path+[i])
#                 # curr_path.pop()
#                 counter[i] += 1
#
#         helper([])
#         return res
# leetcode submit region end(Prohibit modification and deletion)
