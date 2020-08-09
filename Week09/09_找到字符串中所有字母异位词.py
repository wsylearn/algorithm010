# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
#  说明：
#
#
#  字母异位词指字母相同，但排列不同的字符串。
#  不考虑答案输出的顺序。
#
#
#  示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
#  示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#  Related Topics 哈希表
#  👍 331 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded
# class Solution:
#     def get_counts(self, str):
#         counts = [0]*26
#         for s in str:
#             counts[ord(s)-ord("a")] += 1
#         return counts
#
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         p_counts = self.get_counts(p)
#         n_s, n_p = len(s), len(p)
#         ans = []
#         for i in range(n_s - n_p + 1):
#             if self.get_counts(s[i:i+n_p]) == p_counts:
#                 ans.append(i)
#         return ans

# 2 解答成功: 执行耗时:104 ms,击败了94.36% 的Python3用户 内存消耗:14.6 MB,击败了76.10% 的Python3用户
# 滑动窗口
class Solution:
    def get_counts(self, str):
        counts = [0]*26
        for s in str:
            counts[ord(s)-ord("a")] += 1
        return counts

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n_s, n_p = len(s), len(p)
        p_counts = self.get_counts(p)
        s_counts = self.get_counts(s[:n_p])
        ans = []
        if s_counts == p_counts:
            ans.append(0)
        for i in range(n_s - n_p):
            if s[i] != s[i+n_p]:
                s_counts[ord(s[i]) - ord("a")] -= 1
                s_counts[ord(s[i+n_p]) - ord("a")] += 1
            if s_counts == p_counts:
                ans.append(i+1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
