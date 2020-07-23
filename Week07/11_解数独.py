# 编写一个程序，通过已填充的空格来解决数独问题。
#
#  一个数独的解法需遵循如下规则：
#
#
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#
#  空白格用 '.' 表示。
#
#
#
#  一个数独。
#
#
#
#  答案被标成红色。
#
#  Note:
#
#
#  给定的数独序列只包含数字 1-9 和字符 '.' 。
#  你可以假设给定的数独只有唯一解。
#  给定数独永远是 9x9 形式的。
#
#  Related Topics 哈希表 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:136 ms,击败了75.64% 的Python3用户 内存消耗:13.7 MB,击败了11.11% 的Python3用户
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         rows = [set(range(1, 10)) for _ in range(9)]
#         cols = [set(range(1, 10)) for _ in range(9)]
#         blocks = [set(range(1, 10)) for _ in range(9)]
#
#         empty_locations = []
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != ".":
#                     val = int(board[i][j])
#                     rows[i].remove(val)
#                     cols[j].remove(val)
#                     blocks[(i // 3) * 3 + j // 3].remove(val)
#                 else:
#                     empty_locations.append((i, j))
#
#         def backtrack(level=0):
#             if level == len(empty_locations):
#                 return True
#             i, j = empty_locations[level]
#             b = (i // 3) * 3 + j // 3
#             for val in rows[i] & cols[j] & blocks[b]:
#                 board[i][j] = str(val)
#                 rows[i].remove(val)
#                 cols[j].remove(val)
#                 blocks[b].remove(val)
#
#                 if backtrack(level + 1):
#                     return True
#                 rows[i].add(val)
#                 cols[j].add(val)
#                 blocks[b].add(val)
#             return False
#
#         backtrack()

# 2 待修改
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         def solve(board):
#             for i in range(9):
#                 for j in range(9):
#                     if board[i][j] == ".":
#                         for k in range(1, 10):
#                             if is_valida(board, i, j, str(k)):
#                                 board[i][j] = str(k)
#
#                                 if solve(board):
#                                     return True
#                                 else:
#                                     board[i][j] = "."
#                         return False
#
#         def is_valida(board, row, col, k):
#             for index in range(9):
#                 if board[index][col] == k:
#                     return False
#                 if board[row][index] == k:
#                     return False
#                 if board[(row // 3) * 3 + (index // 3)][(col // 3) * 3 + (index % 3)] == k:
#                     return False
#             return True

# leetcode submit region end(Prohibit modification and deletion)
