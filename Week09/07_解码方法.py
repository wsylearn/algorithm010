# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
#  示例 1:
#
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
#  示例 2:
#
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         self.res = 0
#         def helper(s):
#             if len(s) == 0:
#                 self.res += 1
#                 return
#             elif s[0] != "0":
#                 helper(s[1:])
#                 if len(s) >= 2:
#                     if 1 <= int(s[:2]) <= 26:
#                         helper(s[2:])
#         helper(s)
#         return self.res

# 2 解答成功: 执行耗时:52 ms,击败了19.01% 的Python3用户 内存消耗:13.6 MB,击败了6.25% 的Python3用户
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == "0":
#             return 0
#         dp = [0] * (len(s)+1)
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(1, len(s)):
#             if s[i] == "0":
#                 if s[i-1] == "1" or s[i-1] == "2":
#                     dp[i+1] = dp[i-2+1]
#                 else:
#                     return 0
#             else:
#                 if 1 <= int(s[i-1:i+1]) <= 26 and s[i-1] != "0":
#                     dp[i+1] = dp[i-2+1] + dp[i-1+1]
#                 else:
#                     dp[i+1] = dp[i-1+1]
#         return dp[-1]

# 3 解答成功: 执行耗时:48 ms,击败了39.04% 的Python3用户 内存消耗:13.7 MB,击败了6.25% 的Python3用户
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        pre = cur = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    tmp = pre
                else:
                    return 0
            else:
                if s[i-1] != "0" and 1 <=  (10 * int(s[i-1]) + int(s[i])) <= 26:
                    tmp = pre + cur
                else:
                    tmp = cur
            pre, cur = cur, tmp
        return cur



# leetcode submit region end(Prohibit modification and deletion)
