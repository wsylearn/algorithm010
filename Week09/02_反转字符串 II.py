# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
#
#
#  如果剩余字符少于 k 个，则将剩余字符全部反转。
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
#
#
#
#  示例:
#
#  输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
#
#
#  提示：
#
#
#  该字符串只包含小写英文字母。
#  给定字符串的长度和 k 在 [1, 10000] 范围内。
#
#  Related Topics 字符串
#  👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1解答成功: 执行耗时:40 ms,击败了80.61% 的Python3用户 内存消耗:13.8 MB,击败了43.10% 的Python3用户
# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         a = list(s)
#         for i in range(0, len(s), 2*k):
#             a[i:i+k] = reversed(a[i:i+k])
#         return "".join(a)

# 2解答成功: 执行耗时:48 ms,击败了35.20% 的Python3用户 内存消耗:13.5 MB,击败了100.00% 的Python3用户
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        n = len(s)
        for i in range(0, n, 2 * k):
            left = i
            right = min(n - 1, left + k - 1)
            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        return "".join(a)

# leetcode submit region end(Prohibit modification and deletion)
