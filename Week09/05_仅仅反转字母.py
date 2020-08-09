# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#
#
#
#
#
#  示例 1：
#
#  输入："ab-cd"
# 输出："dc-ba"
#
#
#  示例 2：
#
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
#  示例 3：
#
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#  提示：
#
#
#  S.length <= 100
#  33 <= S[i].ASCIIcode <= 122
#  S 中不包含 \ or "
#
#  Related Topics 字符串
#  👍 55 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:48 ms,击败了21.11% 的Python3用户 内存消耗:13.6 MB,击败了66.67% 的Python3用户
# class Solution:
#     def reverseOnlyLetters(self, S: str) -> str:
#         array = list(S)
#         n = len(S)
#         i, j = n-1, 0
#         while i >= 0 and j <= n-1:
#             if S[i].isalpha() and array[j].isalpha():
#                 array[j] = S[i]
#                 i -= 1
#                 j += 1
#             elif not S[i].isalpha():
#                 i -= 1
#             elif not array[j].isalpha():
#                 j += 1
#         return "".join(array)

# 2 解答成功: 执行耗时:44 ms,击败了47.05% 的Python3用户 内存消耗:13.7 MB,击败了32.10% 的Python3用户
# class Solution:
#     def reverseOnlyLetters(self, S: str) -> str:
#         left, right = 0, len(S)-1
#         array = list(S)
#         while left < right:
#             if array[left].isalpha() and array[right].isalpha():
#                 array[left], array[right] = array[right], array[left]
#                 left += 1
#                 right -= 1
#             if not array[left].isalpha():
#                 left += 1
#             if not array[right].isalpha():
#                 right -= 1
#         return "".join(array)

# 3 解答成功: 执行耗时:40 ms,击败了74.53% 的Python3用户 内存消耗:13.6 MB,击败了53.09% 的Python3用户
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters_stack = [s for s in S if s.isalpha()]
        ans = []
        for s in S:
            if s.isalpha():
                ans.append(letters_stack.pop())
            else:
                ans.append(s)
        return "".join(ans)

# leetcode submit region end(Prohibit modification and deletion)
