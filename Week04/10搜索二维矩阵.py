# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  示例 1:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
#  示例 2:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:36 ms,击败了91.43% 的Python3用户 内存消耗:14.6 MB,击败了100.00% 的Python3用户
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         nums = []
#         for r in matrix:
#             nums += r
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = left + (right - left)// 2
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False

# 2 解答成功: 执行耗时:40 ms,击败了78.22% 的Python3用户 内存消耗:14.6 MB,击败了100.00% 的Python3用户
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
#         if target < matrix[0][0] or target > matrix[-1][-1]:
#             return False
#         r_nums, c_nums = len(matrix), len(matrix[0])
#         for r in range(r_nums):
#             if matrix[r][0] <= target <= matrix[r][-1]:
#                 break
#         left, right = 0, c_nums - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if matrix[r][mid] == target:
#                 return True
#             elif matrix[r][mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False

# 3 解答成功: 执行耗时:40 ms,击败了78.22% 的Python3用户 内存消耗:14.5 MB,击败了100.00% 的Python3用户
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        r_nums, c_nums = len(matrix), len(matrix[0])
        r_left, r_right = 0, r_nums-1
        while r_left <= r_right:
            r_mid = r_left + (r_right - r_left) // 2
            if matrix[r_mid][0] <= target <= matrix[r_mid][-1]:
                break
            elif target < matrix[r_mid][0]:
                r_right = r_mid - 1
            else:
                r_left = r_mid + 1

        c_left, c_right = 0, c_nums - 1
        while c_left <= c_right:
            c_mid = c_left + (c_right - c_left) // 2
            if matrix[r_mid][c_mid] == target:
                return True
            elif target < matrix[r_mid][c_mid]:
                c_right = c_mid - 1
            else:
                c_left = c_mid + 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
