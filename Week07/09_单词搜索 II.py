# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#  示例:
#
#  输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
#  说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
#  提示:
#
#
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#  Related Topics 字典树 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:336 ms,击败了35.24% 的Python3用户 内存消耗:28.1 MB,击败了50.00% 的Python3用户
# 字典树
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         if not board or not board[0]:
#             return []
#         if not words:
#             return []
#         self.result = set()
#         self.dx = [-1, 1, 0, 0]
#         self.dy = [0, 0, -1, 1]
#         self.end_mark = "#"
#
#         root = {}
#         for word in words:
#             node = root
#             for c in word:
#                 node = node.setdefault(c, {})
#             node[self.end_mark] = self.end_mark
#
#         self.m, self.n = len(board), len(board[0])
#         for i in range(self.m):
#             for j in range(self.n):
#                 if board[i][j] in root:
#                     self._dfs(board, i, j, "", root)
#         return list(self.result)
#
#     def _dfs(self, board, i, j, cur_word, cur_dict):
#         cur_word += board[i][j]
#         cur_dict = cur_dict[board[i][j]]
#         if self.end_mark in cur_dict:
#             self.result.add(cur_word)
#         tmp, board[i][j] = board[i][j], "@"
#         for k in range(4):
#             x, y = i + self.dx[k], j + self.dy[k]
#             if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != "@" and board[x][y] in cur_dict:
#                 self._dfs(board, x, y, cur_word, cur_dict)
#         board[i][j] = tmp

# 2 解答成功: 执行耗时:300 ms,击败了50.18% 的Python3用户 内存消耗:28.2 MB,击败了50.00% 的Python3用户
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}  # 构造字典树
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited):  # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:  # 已有字典树结束
                res.add(pre)  # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i+di, j+dj
                if 0 <= _i < h and 0 <= _j < w and board[_i][_j] in node and (_i, _j) not in visited:  # 可继续搜索
                    search(_i, _j, node[board[_i][_j]], pre+board[_i][_j], visited | {(_i, _j)})  # dfs搜索

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索
        return list(res)


# leetcode submit region end(Prohibit modification and deletion)
