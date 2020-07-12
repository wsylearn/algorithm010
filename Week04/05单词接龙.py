# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
#
#
#  每次转换只能改变一个字母。
#  转换过程中的中间单词必须是字典中的单词。
#
#
#  说明:
#
#
#  如果不存在这样的转换序列，返回 0。
#  所有单词具有相同的长度。
#  所有单词只由小写字母组成。
#  字典中不存在重复的单词。
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
#  示例 1:
#
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#
#
#  示例 2:
#
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:180 ms,击败了48.52% 的Python3用户 内存消耗:17.3 MB,击败了20.00% 的Python3用户
# O(M×N)，O(M×N)
# 其中 MM 是单词的长度 NN 是单词表中单词的总数。
# from collections import defaultdict
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         if endWord not in wordList or not endWord or not beginWord or not wordList:
#             return 0
#         L = len(beginWord)
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
#         queue = [(beginWord, 1)]
#         visited = {beginWord}
#         while queue:
#             current_word, level = queue.pop(0)
#             for i in range(L):
#                 intermediate_word = current_word[:i] + "*" + current_word[i+1:]
#                 for word in all_combo_dict[intermediate_word]:
#                     if word == endWord:
#                         return level + 1
#                     if word not in visited:
#                         visited.add(word)
#                         queue.append((word, level + 1))
#         return 0

# 1.2 解答成功: 执行耗时:148 ms,击败了70.67% 的Python3用户 内存消耗:17.3 MB,击败了20.00% 的Python3用户
# from collections import defaultdict, deque
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         if endWord not in wordList or not endWord or not beginWord or not wordList:
#             return 0
#         L = len(beginWord)
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
#         queue = deque([(beginWord, 1)])
#         visited = {beginWord}
#         while queue:
#             current_word, level = queue.popleft()
#             for i in range(L):
#                 intermediate_word = current_word[:i] + "*" + current_word[i+1:]
#                 for word in all_combo_dict[intermediate_word]:
#                     if word == endWord:
#                         return level + 1
#                     if word not in visited:
#                         visited.add(word)
#                         queue.append((word, level + 1))
#         return 0

# 2 解答成功: 执行耗时:116 ms,击败了93.47% 的Python3用户 内存消耗:17.1 MB,击败了20.00% 的Python3用户
# O(M×N)，与1法相比，时间变小一般
# O(M×N)，与1法相比，空间变小

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue_begin = [(beginWord, 1)] # BFS starting from beginWord
        queue_end = [(endWord, 1)] # BFS starting from endWord

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
# leetcode submit region end(Prohibit modification and deletion)
