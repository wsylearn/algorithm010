# 颠倒给定的 32 位无符号整数的二进制位。
#
#
#
#  示例 1：
#
#  输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
#
#  示例 2：
#
#  输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
#      因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。
#
#
#
#  提示：
#
#
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -10737418
# 25。
#
#
#
#
#  进阶:
# 如果多次调用这个函数，你将如何优化你的算法？
#  Related Topics 位运算


# leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:44 ms,击败了59.39% 的Python3用户 内存消耗:13.6 MB,击败了15.38% 的Python3用户
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         n = bin(n)[2:]
#         n = "0"*(32-len(n)) + n # n要32位长
#         return int(n[::-1], base=2)

# 1.2 解答成功: 执行耗时:52 ms,击败了15.99% 的Python3用户 内存消耗:13.5 MB,击败了15.38% 的Python3用户
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         return int(("0"*(32+2-len(bin(n))) + bin(n)[2:])[::-1], base=2)

# 2.1 解答成功: 执行耗时:32 ms,击败了97.72% 的Python3用户 内存消耗:13.5 MB,击败了15.38% 的Python3用户
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res, power = 0, 31
#         while n:
#             res += (n & 1) << power
#             n = n >> 1
#             power -= 1
#         return res

# 2.2 解答成功: 执行耗时:44 ms,击败了59.39% 的Python3用户 内存消耗:13.7 MB,击败了15.38% 的Python3用户
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
