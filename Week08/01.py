# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
#
#
#  示例 1：
#
#  输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
#
#  示例 2：
#
#  输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#
#
#  示例 3：
#
#  输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
#
#
#
#  提示：
#
#
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#
#
#
#
#  进阶:
# 如果多次调用这个函数，你将如何优化你的算法？
#  Related Topics 位运算


# leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:44 ms,击败了52.23% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用户
# O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count("1")

# 1.2 解答成功: 执行耗时:40 ms,击败了76.62% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用
# O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         n = bin(n)
#         count = 0
#         for c in n:
#             if c == "1":
#                 count += 1
#         return count

# 2.1 解答成功: 执行耗时:36 ms,击败了91.06% 的Python3用户 内存消耗:13.6 MB,击败了8.33% 的Python3用户
# O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             res = n % 2
#             if res == 1:
#                 count += 1
#             n = n // 2
#         return count

# 2.2 解答成功: 执行耗时:44 ms,击败了52.23% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用户
# O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             res = n % 2
#             if res == 1:
#                 count += 1
#             n = n >> 1
#         return count

# 3 解答成功: 执行耗时:44 ms,击败了52.23% 的Python3用户 内存消耗:13.8 MB,击败了8.33% 的Python3用户
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             res = n & 1
#             if res == 1:
#                 count += 1
#             n = n >> 1
#         return count

# 4 解答成功: 执行耗时:32 ms,击败了97.55% 的Python3用户 内存消耗:13.5 MB,击败了8.33% 的Python3用户
# O(k), k为n中1的个数
# 推荐
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             count += 1
#             n = n & (n-1) # 清空最低位的1
#         return count

# 5 解答成功: 执行耗时:40 ms,击败了76.62% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用户
# O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         mask = 1
#         for _ in range(32):
#             if n & mask != 0:
#                 count += 1
#             mask <<= 1
#         return count

# 6 解答成功: 执行耗时:44 ms,击败了52.23% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用户
# O(K)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return 1 + self.hammingWeight(n&(n-1)) if n else 0

# leetcode submit region end(Prohibit modification and deletion)