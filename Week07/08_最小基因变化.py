# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。
#
#  注意:
#
#
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
#  所有的目标基因序列必须是合法的。
#  假定起始基因序列与目标基因序列是不一样的。
#
#
#  示例 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# 返回值: 1
#
#
#  示例 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# 返回值: 2
#
#
#  示例 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# 返回值: 3
#
#


# leetcode submit region begin(Prohibit modification and deletion)
# 1
# BFS
# from collections import deque
# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         bank = set(bank)
#         if end not in bank:
#             return -1
#         n = len(start)
#         queue = deque([(start, 0)])
#         visited = {start}
#         while queue:
#             node, step = queue.popleft()
#             for i in range(n):
#                 for c in ["A", "C", "G", "T"]:
#                     _node = node[:i] + c + node[i+1:]
#                     if _node not in visited and _node in bank:
#                         if _node == end:
#                             return step + 1
#                         visited.add(_node)
#                         queue.append((_node, step+1))
#         return -1

# 2 解答成功: 执行耗时:40 ms,击败了68.74% 的Python3用户 内存消耗:13.5 MB,击败了100.00% 的Python3用户
# 双向BFS
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        n = len(start)
        distance = 0
        begin = {start}
        stop = {end}
        while begin and stop:
            distance += 1
            next_begin = set()
            for word in begin:
                for i in range(n):
                    for c in ["A", "C", "G", "T"]:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in stop:
                                return distance
                            if new_word in bank:
                                next_begin.add(new_word)
                                bank.remove(new_word)
            begin = next_begin
            if len(stop) < len(begin):
                stop, begin = begin, stop
        return -1

# leetcode submit region end(Prohibit modification and deletion)
