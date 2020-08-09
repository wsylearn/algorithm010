# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#  示例 1:
#
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
#
#
#  注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#  Related Topics 字符串
#  👍 207 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:80 ms,击败了19.29% 的Python3用户 内存消耗:14.4 MB,击败了5.56% 的Python3用户
# class Solution:
#     def reverse(self, s):
#         s = s.strip()
#         l = list(s)
#         i, j = 0, len(l)-1
#         while i < j:
#             l[i], l[j] = l[j], l[i]
#             i += 1
#             j -= 1
#         return "".join(l)
#
#     def reverseWords(self, s: str) -> str:
#         l = s.split()
#         ans = []
#         for w in l:
#             tmp = self.reverse(w)
#             if tmp:
#                 ans.append(tmp)
#         return " ".join(ans)

# 2 解答成功: 执行耗时:36 ms,击败了96.66% 的Python3用户 内存消耗:14 MB,击败了90.37% 的Python3用户
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ans = [w[::-1] for w in s.split()]
#         return " ".join(ans)

# 3 解答成功: 执行耗时:40 ms,击败了90.30% 的Python3用户 内存消耗:13.9 MB,击败了97.78% 的Python3用户
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])[::-1]

# leetcode submit region end(Prohibit modification and deletion)
