# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:36 ms,击败了94.81% 的Python3用户 内存消耗:14.4 MB,击败了7.41% 的Python3用户
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
# leetcode submit region end(Prohibit modification and deletion)
