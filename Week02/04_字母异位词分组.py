# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:64 ms,击败了61.96% 的Python3用户 内存消耗:17 MB,击败了14.29% 的Python3用户
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         tuple2list = defaultdict(list)
#         for s in strs:
#             tuple2list[tuple(sorted(s))].append(s)
#         return list(tuple2list.values())

# 2 解答成功: 执行耗时:72 ms,击败了42.33% 的Python3用户 内存消耗:18.6 MB,击败了14.29% 的Python3用户
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            ans[tuple(counts)].append(s)
        return list(ans.values())

# leetcode submit region end(Prohibit modification and deletion)
