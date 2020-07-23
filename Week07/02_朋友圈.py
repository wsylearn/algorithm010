# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。
#
#  示例 1:
#
#
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#
#
#  示例 2:
#
#
# 输入:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#
#
#  注意：
#
#
#  N 在[1,200]的范围内。
#  对于所有学生，有M[i][i] = 1。
#  如果有M[i][j] = 1，则有M[j][i] = 1。
#
#  Related Topics 深度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:252 ms,击败了48.18% 的Python3用户 内存消耗:14.5 MB,击败了11.11% 的Python3用户
# DFS
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         def dfs(i):
#             for j in range(len(M)):
#                 if M[i][j] == 1 and visited[j] == 0:
#                     visited[j] = 1
#                     dfs(j)
#         visited = [0] * len(M)
#         count = 0
#         for i in range(len(M)):
#             if visited[i] == 0:
#                 dfs(i)
#                 count += 1
#
#         return count

# 2 解答成功: 执行耗时:236 ms,击败了68.16% 的Python3用户 内存消耗:13.9 MB,击败了11.11% 的Python3用户
# BFS
import collections
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m = len(M)
        res = 0
        visited = [0] * m
        for i in range(m):
            if visited[i] == 0:
                visited[i] = 1
                res += 1
                neighbors = collections.deque([i])
                while neighbors:
                    node = neighbors.popleft()
                    for j in range(m):
                        if visited[j] == 0 and M[node][j] == 1:
                            visited[j] = 1
                            neighbors.append(j)
        return res

# 3 解答成功: 执行耗时:256 ms,击败了44.97% 的Python3用户 内存消耗:13.6 MB,击败了11.11% 的Python3用户
# 并查集
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         if not M:
#             return 0
#         n = len(M)
#         p = [i for i in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if M[i][j] == 1:
#                     self._union(p, i, j)
#         return len(set([self._parent(p, k) for k in range(n)]))
#
#     def _union(self, p, i, j):
#         p1 = self._parent(p, i)
#         p2 = self._parent(p, j)
#         p[p2] = p1
#
#     def _parent(self, p, i):
#         root = i
#         while p[root] != root:
#             root = p[root]
#         while p[i] != i:
#             old_i = i
#             i = p[old_i]
#             p[old_i] = root
#         return root

# leetcode submit region end(Prohibit modification and deletion)
