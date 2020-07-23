# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:144 ms,击败了5.27% 的Python3用户 内存消耗:20.3 MB,击败了6.06% 的Python3用户
# class Solution:
#     def helper(self, level, n, s):
#         if level > 2*n:
#             return [s]
#         level += 1
#         return self.helper(level, n, s + "(") + self.helper(level, n, s + ")")
#
#     def is_right(self, s):
#         if s[0] == ")":
#             return False
#         stack = ["?"]
#         pun_cp = {"?":"?", "(":")"}
#         for i in s:
#             if i == "(":
#                 stack.append("(")
#             else:
#                 tmp = stack.pop()
#                 if pun_cp[tmp] != i:
#                     return False
#         return len(stack) == 1
#
#     def generateParenthesis(self, n: int):
#         all = self.helper(1, n, "")
#         return [i for i in all if self.is_right(i)]

# class Solution:
#     def helper(self, n, s):
#         if len(s) == 2 * n:
#             return [s]
#         return self.helper(n, s + "(") + self.helper(n, s + ")")
#
#     def is_valida(self, s):
#         stack = ["?"]
#         cp = {"(": ")", "?": "?"}
#         for i in s:
#             if i == "(":
#                 stack.append("(")
#             else:
#                 tmp = stack.pop()
#                 if tmp != "(":
#                     return False
#         return len(stack) == 1
#
#     def generateParenthesis(self, n: int) -> List[str]:
#         all_res = self.helper(n, "")
#         return [i for i in all_res if self.is_valida(i)]

# class Solution:
#     def helper(self, n):
#         res = [""]
#         for _ in range(2*n):
#             tmp = []
#             for i in res:
#                 tmp.append(i+"(")
#                 tmp.append(i+")")
#             res = tmp
#         return res
#
#     def is_vailda(self, s):
#         stack = ["?"]
#         cp = {"(" : ")", "?" : "?"}
#         for i in s:
#             if i in cp:
#                 stack.append(i)
#             else:
#                 tmp = stack.pop()
#                 if cp[tmp] != i:
#                     return False
#         return len(stack) == 1
#
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = self.helper(n)
#         return [i for i in res if self.is_vailda(i)]


# 2 解答成功: 执行耗时:44 ms,击败了64.72% 的Python3用户 内存消耗:13.6 MB,击败了6.06% 的Python3用户
# 无论进行到哪一步了，只要1）做括号的个数大于n ；2）右括号的个数大于左括号。就一定非法，后面怎么修改都于事无补
# O(2**n)
# class Solution:
#     def helper(self, left, right, n, s, res):
#         if left == n and right == n:
#             res.append(s)
#             return
#         if left < n:
#             self.helper(left+1, right, n, s+"(",res)
#         if right < left:
#             self.helper(left, right+1, n, s+")",res)
#
#     def generateParenthesis(self, n: int):
#         res = []
#         self.helper(0,0,n,"",res)
#         return res

# class Solution:
#     def helper(self, left, right, n, s):
#         if left == n and right == n:
#             self.res.append(s)
#         if left < n:
#             self.helper(left+1, right, n, s+"(")
#         if right < left:
#             self.helper(left, right+1, n, s+")")
#
#     def generateParenthesis(self, n: int):
#         self.res = []
#         self.helper(0,0,n,"")
#         return self.res

# class Solution:
#     def helper(self, left, right, n, s):
#         if left == n and right == n:
#             return [s]
#         res = []
#         if left < n:
#             res += self.helper(left+1, right, n, s+"(")
#         if right < left:
#             res += self.helper(left, right+1, n, s+")")
#         return res
#
#     def generateParenthesis(self, n: int):
#         return self.helper(0,0,n,"")

# 3.1
#BFS
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = ["(", ")"]
#         res = []
#         while stack:
#             pun = stack.pop(0)
#             if len(pun) == 2 * n:
#                 res.append(pun)
#                 continue
#             stack.append(pun + "(")
#             stack.append(pun + ")")
#
#         def is_valida(s):
#             stack = ["?"]
#             for i in s:
#                 if i == "(":
#                     stack.append(i)
#                 else:
#                     if stack.pop() != "(":
#                         return False
#             return len(stack) == 1
#
#         return [s for s in res if is_valida(s)]
#
# #3.2
# dfs
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = [("(",1,0)]
#         res = []
#         while stack:
#             pun, left, right = stack.pop(0)
#             if left == right == n:
#                 res.append(pun)
#                 continue
#             if left < n:
#                 stack.append((pun + "(", left+1, right))
#             if right < left:
#                 stack.append((pun + ")", left, right+1))
#         return res

# 3.3 解答成功: 执行耗时:40 ms,击败了83.79% 的Python3用户 内存消耗:14 MB,击败了6.06% 的Python3用
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = deque([("(",1,0)])
        res = []
        while stack:
            pun, left, right = stack.popleft()
            if left == right == n:
                res.append(pun)
                continue
            if left < n:
                stack.append((pun + "(", left+1, right))
            if right < left:
                stack.append((pun + ")", left, right+1))
        return res
# leetcode submit region end(Prohibit modification and deletion)
