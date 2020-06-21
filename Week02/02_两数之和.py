# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:68 ms,击败了60.58% 的Python3用户 内存消耗:15.3 MB,击败了5.48% 的Python3用户
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_id_list = [(n, i) for i,n in enumerate(nums)]
#         num_id_list.sort()
#         left, right = 0, len(nums)-1
#         while left < right:
#             if num_id_list[left][0] + num_id_list[right][0] < target:
#                 left += 1
#             elif num_id_list[left][0] + num_id_list[right][0] > target:
#                 right -= 1
#             else:
#                 return [num_id_list[left][1], num_id_list[right][1]]

# 2 解答成功: 执行耗时:68 ms,击败了60.58% 的Python3用户 内存消耗:15.8 MB,击败了5.48% 的Python3用户
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num2id = {n:i for i,n in enumerate(nums)}
#         for i in range(len(nums)):
#             j = num2id.get(target - nums[i])
#             if j and i != j:
#                 return [i, j]

# 3 解答成功: 执行耗时:6568 ms,击败了7.23% 的Python3用户 内存消耗:14.5 MB,击败了13.41% 的Python3用户
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# 4 解答成功: 执行耗时:60 ms,击败了76.02% 的Python3用户 内存消耗:15.1 MB,击败了5.48% 的Python3用户
# 一遍哈希
class Solution:
    def twoSum(self, nums, target):
        num2id = {}
        for i in range(len(nums)):
            j = num2id.get(target - nums[i])
            if j is not None and i != j:
                return [j, i]
            num2id[nums[i]] = i
# leetcode submit region end(Prohibit modification and deletion)
