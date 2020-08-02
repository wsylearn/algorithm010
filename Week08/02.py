# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
#  示例 1:
#
#  输入: 1
# 输出: true
# 解释: 20 = 1
#
#  示例 2:
#
#  输入: 16
# 输出: true
# 解释: 24 = 16
#
#  示例 3:
#
#  输入: 218
# 输出: false
#  Related Topics 位运算 数学


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:40 ms,击败了83.54% 的Python3用户 内存消耗:13.7 MB,击败了6.25% 的Python3用户
# O(k)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and n&(n-1) == 0

# 2 解答成功: 执行耗时:44 ms,击败了63.89% 的Python3用户 内存消耗:13.7 MB,击败了6.25% 的Python3用户
# O(n)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = bin(n)
        return n.count("1") == 1
# leetcode submit region end(Prohibit modification and deletion)
