# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  你可以假设数组中不存在重复元素。
#
#  示例 1:
#
#  输入: [3,4,5,1,2]
# 输出: 1
#
#  示例 2:
#
#  输入: [4,5,6,7,0,1,2]
# 输出: 0
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:32 ms,击败了96.79% 的Python3用户 内存消耗:13.8 MB,击败了6.67% 的Python3用户
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:  # [1,2,3]
#             return nums[left]
#         if nums[right - 1] >= nums[right]:  # [2,1],[2,3,4,1]
#             return nums[right]
#         while left <= right:
#             mid = (left + right) // 2
#             if mid == left:  # left=0,right=1,mid=0
#                 return nums[left]
#             elif nums[mid - 1] >= nums[mid] and nums[mid] <= nums[mid + 1]:
#                 return nums[mid]
#             elif nums[mid] >= nums[left]:
#                 left = mid
#             else:
#                 right = mid
# 2 解答成功: 执行耗时:36 ms,击败了88.79% 的Python3用户 内存消耗:13.9 MB,击败了6.67% 的Python3用户
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:  # [1,2,3]
#             return nums[left]
#         if nums[right - 1] >= nums[right]:  # [2,1],[2,3,4,1]
#             return nums[right]
#         while left <= right:
#             mid = left + (right - left) // 2
#             # if mid == left:  # left=0,right=1,mid=0
#             #     return nums[left]
#             if nums[mid - 1] >= nums[mid] and nums[mid] <= nums[mid + 1]:
#                 return nums[mid]
#             elif nums[mid] >= nums[left]:
#                 left = mid
#             else:
#                 right = mid

# 3.1 解答成功: 执行耗时:36 ms,击败了88.79% 的Python3用户 内存消耗:13.5 MB,击败了6.67% 的Python3用户
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:  # [1,2,3]
#             return nums[left]
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] > nums[mid+1]:
#                 return nums[mid+1]
#             if nums[mid-1] > nums[mid]:
#                 return nums[mid]
#             if nums[mid] > nums[left]:
#                 left = mid
#             else:
#                 right = mid

# 3.2 解答成功: 执行耗时:36 ms,击败了88.79% 的Python3用户 内存消耗:13.6 MB,击败了6.67% 的Python3用户
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         # if len(nums) == 1:
#         #     return nums[0]
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:  # [1,2,3]
#             return nums[left]
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] > nums[mid+1]:
#                 return nums[mid+1]
#             if nums[mid-1] > nums[mid]: # 不能省略
#                 return nums[mid]
#             if nums[mid] > nums[left]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

# 3.3 解答成功: 执行耗时:36 ms,击败了88.79% 的Python3用户 内存消耗:13.6 MB,击败了6.67% 的Python3用户
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         # if len(nums) == 1:
#         #     return nums[0]
#         left, right = 0, len(nums) - 1
#         if nums[left] <= nums[right]:  # [1,2,3]
#             return nums[left]
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] > nums[mid+1]:
#                 return nums[mid+1]
#             # if nums[mid-1] > nums[mid]:
#             #     return nums[mid]
#             if nums[mid] > nums[left]:
#                 left = mid
#             else:
#                 right = mid

# leetcode submit region end(Prohibit modification and deletion)
