# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
#  示例 1:
#
#
# 输入: "aba"
# 输出: True
#
#
#  示例 2:
#
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
#
#  注意:
#
#
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
#
#  Related Topics 字符串
#  👍 241 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1解答成功: 执行耗时:188 ms,击败了49.11% 的Python3用户 内存消耗:14.3 MB,击败了12.68% 的Python3用户
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def search(chars, times):
#             begin, end = 0, len(chars)-1
#             while begin < end:
#                 if chars[begin] != chars[end]:
#                     if times == 0:
#                         return False
#                     return search(chars[begin:end], times-1) or search(chars[begin+1:end+1], times-1)
#                 begin += 1
#                 end -= 1
#             return True
#         return search(s, 1)

# 2 解答成功: 执行耗时:116 ms,击败了77.69% 的Python3用户 内存消耗:14.2 MB,击败了25.35% 的Python3用户
class Solution:
    def is_Palindrom(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_Palindrom(s[left + 1:right + 1]) or self.is_Palindrom(s[left:right])
            left += 1
            right -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
