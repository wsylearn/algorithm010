# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#  你可以假设数组中不存在重复的元素。
#
#  你的算法时间复杂度必须是 O(log n) 级别。
#
#  示例 1:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
#  示例 2:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# 1 基础的暴力法 O(n),不符合题意
# 解答成功: 执行耗时:48 ms,击败了23.04% 的Python3用户 内存消耗:13.7 MB,击败了7.69% 的Python3用户
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         return nums.index(target)

# 2 改造后的暴力法，将nums还原为完全升序，再用二分查找
# 2.1 不符合题意
# O（n）
# 解答成功: 执行耗时:44 ms,击败了49.84% 的Python3用户 内存消耗:14.1 MB,击败了7.69% 的Python3用户
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         val2index = {v:i for i,v in enumerate(nums)}
#         min_val = nums[0]
#         min_val_index = 0
#         for i in range(1, len(nums)):
#             if nums[i] < min_val:
#                 min_val = nums[i]
#                 min_val_index = i
#         nums[::] = nums[min_val_index:] + nums[:min_val_index]
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return val2index[nums[mid]]
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1

# 2.2 不符合题意
# O（n）
# 解答成功: 执行耗时:40 ms,击败了74.44% 的Python3用户 内存消耗:14 MB,击败了7.69% 的Python3用户
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         val2index = {v:i for i,v in enumerate(nums)}
#         nums.sort()
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return val2index[nums[mid]]
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1

# 2.3
# 可以类比153题，通过二分查找，找到最小值，还原nums变为原来序列。在通过二分查找是否含有target这个值。
# （但是，如果返回的是原来位置索引，是不是要有个表记录原来的索引，还是要遍历原来的数组，时间还是O（n）？）

# 3 解答成功: 执行耗时:36 ms,击败了90.58% 的Python3用户 内存消耗:13.9 MB,击败了7.69% 的Python3用户
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left < right: # 此法中不能有=号
#             mid = left + (right - left) // 2
#             if (nums[0] <= nums[mid]) and (target > nums[mid] or target < nums[0]):
#                 left = mid + 1 #此法中，不加1不行
#             elif (nums[0] > nums[mid]) and (target > nums[mid] and target < nums[0]):
#                 left = mid + 1 #此法中，不加1不行
#             else:
#                 right = mid   #此法中，不能加1
#         if left == right and nums[left] == target:
#             return left
#         else:
#             return -1



# leetcode submit region end(Prohibit modification and deletion)
