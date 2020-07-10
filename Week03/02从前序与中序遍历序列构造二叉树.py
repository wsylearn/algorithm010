# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics 树 深度优先搜索 数组


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1 解答成功: 执行耗时:228 ms,击败了23.89% 的Python3用户 内存消耗:87.5 MB,击败了11.11% 的Python3用户
# O(n)
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder or not inorder:
#             return None
#         root = TreeNode(preorder[0])
#         root_index = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
#         root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
#         return root


# 2 解答成功: 执行耗时:48 ms,击败了96.60% 的Python3用户 内存消耗:18.2 MB,击败了100.00% 的Python3用户
# O(n), O(n)
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
#             if preorder_left > preorder_right:
#                 return None
#
#             # 前序遍历中的第一个节点就是根节点
#             preorder_root = preorder_left
#             # 在中序遍历中定位根节点
#             inorder_root = index[preorder[preorder_root]]
#
#             # 先把根节点建立出来
#             root = TreeNode(preorder[preorder_root])
#             # 得到左子树中的节点数目
#             size_left_subtree = inorder_root - inorder_left
#             # 递归地构造左子树，并连接到根节点
#             # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
#             root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
#                                     inorder_root - 1)
#             # 递归地构造右子树，并连接到根节点
#             # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
#             root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
#                                      inorder_right)
#             return root
#
#         n = len(preorder)
#         # 构造哈希映射，帮助我们快速定位根节点
#         index = {element: i for i, element in enumerate(inorder)}
#         return myBuildTree(0, n - 1, 0, n - 1)

# 3 解答成功: 执行耗时:52 ms,击败了92.59% 的Python3用户 内存消耗:18.2 MB,击败了100.00% 的Python3用户
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        val2index_dic = {v : i for i, v in enumerate(inorder)}
        def helper(preorder_left, inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return
            root = TreeNode(preorder[preorder_left])
            root_index = val2index_dic[preorder[preorder_left]]
            l = root_index - inorder_left
            root.left = helper(preorder_left + 1, inorder_left, root_index - 1)
            root.right = helper(preorder_left + l + 1, root_index + 1, inorder_right)
            return root
        return helper(0, 0, len(inorder)-1)

# leetcode submit region end(Prohibit modification and deletion)
