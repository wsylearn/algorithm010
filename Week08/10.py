# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
#  你需要返回给定数组中的重要翻转对的数量。
#
#  示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
#  示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
#  注意:
#
#
#  给定数组的长度不会超过50000。
#  输入数组中的所有数字都在32位整数的表示范围内。
#
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         self.tmp = [0] * n
#         return self.merge_sort(nums, 0, n-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j, k = left, mid + 1, left
#         while i <= mid and j <= right:
#             if nums[i] > nums[j]:
#                 self.tmp[k] = nums[j]
#                 if nums[i] > 2 * nums[j]:
#                     inv_count += mid - i + 1
#                 j += 1
#             else:
#                 self.tmp[k] = nums[i]
#                 i += 1
#             k += 1
#         while i <= mid:
#             self.tmp[k] = nums[i]
#             if nums[i] > 2 * nums[j-1]:
#                 inv_count += mid - i + 1
#             k += 1
#             i += 1
#         while j <= right:
#             self.tmp[k] = nums[j]
#             k += 1
#             j += 1
#         nums[left:right+1] = self.tmp[left:right+1]
#         return inv_count

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         self.tmp = [0] * n
#         return self.merge_sort(nums, 0, n-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j, k = left, mid + 1, left
#         while i <= mid and j <= right:
#             if nums[i] <= 2 * nums[j]:
#                 self.tmp[k] = nums[i]
#                 inv_count += (j - (mid + 1))
#                 i += 1
#             else:
#                 self.tmp[k] = nums[j]
#                 j += 1
#             k += 1
#         while i <= mid:
#             self.tmp[k] = nums[i]
#             if nums[i] <= 2 * nums[j-1]:
#                 inv_count += (j - (mid + 1))
#             k += 1
#             i += 1
#         while j <= right:
#             self.tmp[k] = nums[j]
#             k += 1
#             j += 1
#         nums[left:right+1] = self.tmp[left:right+1]
#         return inv_count

# 解答失败: 测试用例:[2,4,3,5,1] 测试结果:2 期望结果:3 stdout:

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         self.tmp = [0] * n
#         return self.merge_sort(nums, 0, n-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j, k = left, mid + 1, left
#         while i <= mid and j <= right:
#             if nums[i] <= 2 * nums[j]:
#                 self.tmp[k] = nums[i]
#                 inv_count += (j - (mid + 1))
#                 i += 1
#             else:
#                 self.tmp[k] = nums[j]
#                 j += 1
#             k += 1
#         while i <= mid:
#             self.tmp[k] = nums[i]
#             # if nums[i] <= 2 * nums[j-1]:
#             #     inv_count += (j - (mid + 1))
#             k += 1
#             i += 1
#         while j <= right:
#             self.tmp[k] = nums[j]
#             k += 1
#             j += 1
#         nums[left:right+1] = self.tmp[left:right+1]
#         return inv_count


# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         return self.merge_sort(nums, 0, len(nums)-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j = left, mid + 1
#         while i <= mid and j <= right:
#             if nums[i] <= 2 * nums[j]:
#                 inv_count += (j - (mid + 1))
#                 i += 1
#             else:
#                 j += 1
#         if j == right + 1 and nums[i] > 2 * nums[right]:
#             inv_count += (j - (mid + 1))
#         nums[left:right+1] = sorted(nums[left:right+1])
#         return inv_count

# 解答失败: 测试用例:[2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
# 测试结果:8 期望结果:9 stdout:

# 1 解答成功: 执行耗时:1880 ms,击败了82.65% 的Python3用户 内存消耗:20.8 MB,击败了56.25% 的Python3用户
# O(nlogn * logn) 乘以logn是因为没有归并，直接调用了自带的sorted
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         return self.merge_sort(nums, 0, len(nums)-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j = left, mid + 1
#         while i <= mid:
#             while j <= right and nums[i] > 2*nums[j]:
#                 j += 1
#             inv_count += j - (mid+1)
#             i += 1
#         nums[left:right+1] = sorted(nums[left:right+1])
#         return inv_count

# 2
# O(nlogn * logn) 乘以logn是因为没有归并，直接调用了自带的sorted
# 2.1解答成功: 执行耗时:2000 ms,击败了81.47% 的Python3用户 内存消耗:20.7 MB,击败了62.50% 的Python3用户
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         self.inv_count = 0
#         self.merge_sort(nums, 0, len(nums)-1)
#         return self.inv_count
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         self.merge_sort(nums, left, mid)
#         self.merge_sort(nums, mid+1, right)
#         count = 0
#         i, j = left, mid + 1
#         while i <= mid:
#             if j > right or nums[i] <= 2 * nums[j]:
#                 self.inv_count += count
#                 i += 1
#             else:
#                 count += 1
#                 j += 1
#         nums[left:right+1] = sorted(nums[left:right+1])

# 2.2 通过 1924 ms	20.6 MB
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         return self.merge_sort(nums, 0, len(nums)-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, j = left, mid + 1
#         while i <= mid:
#             if j > right or nums[i] <= 2 * nums[j]:
#                 inv_count += j - (mid+1)
#                 i += 1
#             else:
#                 j += 1
#         nums[left:right+1] = sorted(nums[left:right+1])
#         return inv_count

# 3 O(nlogn)
# 3.1 解答成功: 执行耗时:2716 ms,击败了43.24% 的Python3用户 内存消耗:20.1 MB,击败了100.00% 的Python3用户
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         return self.merge_sort(nums, 0, len(nums)-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         cache = [0] * (right - left + 1)
#         i, t, c = left, left, 0
#         for j in range(mid+1, right+1):
#             while i <= mid and nums[i] <= 2 * nums[j]:
#                 i += 1
#             while t <= mid and nums[t] < nums[j]:
#                 cache[c] = nums[t]
#                 c += 1
#                 t += 1
#             cache[c] = nums[j]
#             count += mid - i + 1
#             c += 1
#
#         while t <= mid:
#             cache[c] = nums[t]
#             c += 1
#             t += 1
#
#         nums[left:right+1] = cache
#         return count

# 3.2 解答成功: 执行耗时:2676 ms,击败了47.06% 的Python3用户 内存消耗:21.2 MB,击败了6.25% 的Python3用户
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         self.tmp = [0] * n
#         return self.merge_sort(nums, 0, n-1)
#
#     def merge_sort(self, nums, left, right):
#         if left >= right:
#             return 0
#         mid = (left + right) >> 1 # (left + right) // 2
#         inv_count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
#         i, t, k = left, left, left
#         for j in range(mid+1, right+1):
#             while i <= mid and nums[i] <= 2 * nums[j]:
#                 i += 1
#             while t <= mid and nums[t] < nums[j]:
#                 self.tmp[k] = nums[t]
#                 k += 1
#                 t += 1
#             self.tmp[k] = nums[j]
#             inv_count += mid - i + 1
#             k += 1
#
#         while t <= mid:
#             self.tmp[k] = nums[t]
#             k += 1
#             t += 1
#
#         nums[left:right+1] = self.tmp[left:right+1]
#         return inv_count

# 4 解答成功: 执行耗时:1448 ms,击败了100.00% 的Python3用户 内存消耗:20.9 MB,击败了31.25% 的Python3用户
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         import bisect
#         arr = []
#         res = 0
#         for num in nums:
#             res += len(arr) - bisect.bisect_right(arr, num * 2)
#             # bisect.insort(arr, num)
#             loc = bisect.bisect_right(arr, num)
#             arr[loc:loc] = [num]
#         return res

# leetcode submit region end(Prohibit modification and deletion)
