# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
#
#  示例 1：
#
#  输入: "the sky is blue"
# 输出: "blue is sky the"
#
#
#  示例 2：
#
#  输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
#
#  示例 3：
#
#  输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  说明：
#
#
#  无空格字符构成一个单词。
#  输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#  如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  进阶：
#
#  请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
#  Related Topics 字符串
#  👍 203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:36 ms,击败了91.42% 的Python3用户 内存消耗:13.9 MB,击败了52.09% 的Python3用户
# O(N)
# O(N)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))

# 2 88 ms	14.1 MB
# class Solution:
#     def reverse(self, str):
#         left, right = 0, len(str) - 1
#         while left < right:
#             if str[left] == " ":
#                 left += 1
#             if str[right] == " ":
#                 right -= 1
#             if str[left] != " " and str[right] != " ":
#                 break
#         L = list(str[left:right+1])
#         i, j = 0, len(L) - 1
#         while i < j:
#             L[i], L[j] = L[j], L[i]
#             i += 1
#             j -= 1
#         return "".join(L)
#
#     def reverseWords(self, s: str) -> str:
#         r_s = self.reverse(s)
#         n = len(r_s)
#         ans = []
#         i = 0
#         while i < n:
#             j = i + 1
#             while True:
#                 if j >= n or r_s[j] == " ":
#                     tmp = self.reverse(r_s[i:j])
#                     if " " not in tmp:
#                         ans.append(tmp)
#                     i = j + 1
#                     break
#                 else:
#                     j += 1
#
#         return " ".join(ans)

# 3 解答成功: 执行耗时:88 ms,击败了5.53% 的Python3用户 内存消耗:14.1 MB,击败了6.46% 的Python3用户
# class Solution:
#     def reverse(self, str):
#         s = str.strip()
#         L = list(s)
#         i, j = 0, len(L) - 1
#         while i < j:
#             L[i], L[j] = L[j], L[i]
#             i += 1
#             j -= 1
#         return "".join(L)
#
#     def reverseWords(self, s: str) -> str:
#         r_s = self.reverse(s)
#         n = len(r_s)
#         ans = []
#         i = 0
#         while i < n:
#             j = i + 1
#             while True:
#                 if j >= n or r_s[j] == " ":
#                     tmp = self.reverse(r_s[i:j])
#                     if tmp:
#                         ans.append(tmp)
#                     i = j + 1
#                     break
#                 else:
#                     j += 1
#
#         return " ".join(ans)

# 4 解答成功: 执行耗时:32 ms,击败了97.39% 的Python3用户 内存消耗:13.9 MB,击败了58.14% 的Python3用户
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()[::-1]
        ls = s.split()
        for i in range(len(ls)):
            ls[i] = ls[i][::-1]
        return " ".join(ls)

# leetcode submit region end(Prohibit modification and deletion)
