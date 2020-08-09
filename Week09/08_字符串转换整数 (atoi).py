# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
#  首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
#
#  如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
#  假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
#  该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
#
#
#  注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
#  在任何情况下，若函数不能进行有效的转换时，请返回 0 。
#
#  提示：
#
#
#  本题中的空白字符只包括空格字符 ' ' 。
#  假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回 INT_MAX (231
#  − 1) 或 INT_MIN (−231) 。
#
#
#
#
#  示例 1:
#
#  输入: "42"
# 输出: 42
#
#
#  示例 2:
#
#  输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
#
#  示例 3:
#
#  输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
#
#  示例 4:
#
#  输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
#
#  示例 5:
#
#  输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。
#
#  Related Topics 数学 字符串
#  👍 779 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:40 ms,击败了91.73% 的Python3用户 内存消耗:13.8 MB,击败了14.32% 的Python3用户
# import re
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         res = re.findall(r"^\s*[+-]?\d+", str)
#         if not res:
#             return 0
#         res = int(res[0])
#         if res > 2**31 - 1:
#             return 2**31 - 1
#         if res < -2**31:
#             return -2**31
#         return res

# 2 解答成功: 执行耗时:44 ms,击败了78.44% 的Python3用户 内存消耗:13.7 MB,击败了42.06% 的Python3用户
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         i = 0
#         n = len(str)
#         while i < n and str[i] == ' ':
#             i = i + 1
#         if n == 0 or i == n:
#             return 0
#         flag = 1
#         if str[i] == '-':
#             flag = -1
#         if str[i] == '+' or str[i] == '-':
#             i = i + 1
#         INT_MAX = 2 ** 31 - 1
#         INT_MIN = -2 ** 31
#         ans = 0
#         while i < n and '0' <= str[i] <= '9':
#             ans = ans * 10 + int(str[i]) - int('0')
#             i += 1
#             if (ans - 1 > INT_MAX):
#                 break
#
#         ans = ans * flag
#         if ans > INT_MAX:
#             return INT_MAX
#         if ans < INT_MIN:
#             return INT_MIN
#         return ans

# 3 解答成功: 执行耗时:48 ms,击败了58.30% 的Python3用户 内存消耗:13.8 MB,击败了15.65% 的Python3用户
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         ans, index, sign, n = 0, 0, 1, len(str)
#         # 1 empty string
#         if n == 0:
#             return 0
#         # 2 remove spaces
#         while index < n and str[index] == " ": # index < n 在前面
#             index += 1
#         # 3 handle signs
#         if index < n: # 防止" "
#             if str[index] == "+" or str[index] == "-":
#                 sign = 1 if str[index] == "+" else -1
#                 index += 1
#         # 4 convert number and avoid overflow
#         INT_MAX = 2 ** 31 - 1
#         INT_MIN = -2 ** 31
#         while index < n:
#             digit = ord(str[index]) - ord("0")
#             if digit < 0 or digit > 9:
#                 break
#             ans = 10 * ans + digit
#             # check if ans orverflow
#             if sign * ans > INT_MAX or sign * ans < INT_MIN:
#                 return INT_MAX if sign == 1 else INT_MIN
#             index += 1
#         return sign * ans

# 4 解答成功: 执行耗时:64 ms,击败了5.74% 的Python3用户 内存消耗:13.8 MB,击败了16.97% 的Python3用户
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        list_str = list(str.strip())
        sign = -1 if list_str[0] == "-" else 1
        if list_str[0] in ["+", "-"]:
            del list_str[0]
        ans, i = 0, 0
        while i < len(list_str) and list_str[i].isdigit():
            ans = 10*ans + ord(list_str[i]) - ord("0")
            i += 1
        # return max(min(sign*ans, 2**31-1), -2**31)
        return min(max(sign*ans, -2**31), 2**31-1)


# leetcode submit region end(Prohibit modification and deletion)
