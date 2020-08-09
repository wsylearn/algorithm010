# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划
#  👍 2517 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


# 1 暴力m枚举起点和终点O（n^3）
# 运行失败: Time Limit Exceeded
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def isPalindrome(s):
#             return s == s[::-1]
#         ans = ""
#         visited = set()
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 if s[i:j] not in visited:
#                     if isPalindrome(s[i:j]) and len(s[i:j]) > len(ans):
#                         ans = s[i:j]
#                     visited.add(s[i:j])
#         return ans

# 2 解答成功: 执行耗时:960 ms,击败了83.15% 的Python3用户 内存消耗:13.7 MB,击败了76.26% 的Python3用户
# 枚举字符串中间字母
# O（n^2）
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def extend_Palindrome(s, left, right):
#             while left >= 0 and right <= n-1 and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             if right - left - 1 > self.max_len:
#                 self.lo = left + 1
#                 self.max_len = right - left - 1
#
#         n = len(s)
#         if n < 2:
#             return s
#         self.lo = self.max_len = 0
#         for i in range(n):
#             extend_Palindrome(s, i, i)
#             extend_Palindrome(s, i, i+1)
#         return s[self.lo:self.lo+self.max_len]

# 3
# 3.1 解答成功: 执行耗时:4052 ms,击败了46.56% 的Python3用户 内存消耗:21.4 MB,击败了34.91% 的Python3用户
# 动态规划
# P(i, j)代表s[i:j+1]是不是回文串（注意，i，j都是索引）
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         res = ""
#         dp = [[0]*n for _ in range(n)]
#         for i in range(n-1, -1, -1):
#             for j in range(i, n):
#                 dp[i][j] = (s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]))
#
#                 if dp[i][j] and j+1-i > len(res):
#                     res = s[i:j+1]
#         return res

# 3.2解答成功: 执行耗时:4216 ms,击败了44.83% 的Python3用户 内存消耗:21.5 MB,击败了17.22% 的Python3用户
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

                if dp[i][j] and j+1-i > len(res):
                    res = s[i:j+1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
