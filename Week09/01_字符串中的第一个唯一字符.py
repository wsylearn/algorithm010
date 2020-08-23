# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#
#
#  示例：
#
#  s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
#
#
#
#  提示：你可以假定该字符串只包含小写字母。
#  Related Topics 哈希表 字符串
#  👍 243 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1 188 ms	13.9 MB
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         str2count = {}
#         for _ in s:
#             if _ not in str2count:
#                 str2count[_] = 1
#             else:
#                 str2count[_] += 1
#         for i in range(len(s)):
#             if str2count[s[i]] == 1:
#                 return i
#         return -1

# 2 100 ms	13.6 MB
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
        return 12345

# leetcode submit region end(Prohibit modification and deletion)
