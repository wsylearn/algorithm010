# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
#  示例 1:
#
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#
#  示例 2:
#
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#
#  说明:
#
#
#  所有节点的值都是唯一的。
#  p、q 为不同节点且均存在于给定的二叉树中。
#
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 解答成功: 执行耗时:96 ms,击败了42.90% 的Python3用户 内存消耗:24 MB,击败了33.33% 的Python3用户
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root or root is p or root is q:
#             return root
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
#         if not left:
#             return right
#         if not right:
#             return left
#         return root

# 2 解答成功: 执行耗时:92 ms,击败了56.50% 的Python3用户 内存消耗:17.9 MB,击败了100.00% 的Python3用户
# 中序遍历
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         inorder = []
#         stack = [(False,root)]
#         while stack:
#             flag, node = stack.pop()
#             if not node:
#                 continue
#             if not flag:
#                 stack.append((False, node.right))
#                 stack.append((True, node))
#                 stack.append((False, node.left))
#             else:
#                 inorder.append(node.val)
#
#         val2index_dict = {x:i for i,x in enumerate(inorder)}
#         p_index = val2index_dict[p.val]
#         q_index = val2index_dict[q.val]
#         node = root
#         node_index = val2index_dict[root.val]
#         while (p_index-node_index)*(q_index-node_index) > 0:
#             if p_index-node_index < 0:
#                 node = node.left
#                 node_index = val2index_dict[node.val]
#             else:
#                 node = node.right
#                 node_index = val2index_dict[node.val]
#
#         return node

# 3解答成功: 执行耗时:100 ms,击败了33.18% 的Python3用户 内存消耗:28.4 MB,击败了9.52% 的Python3用户
# 链表相遇
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         dic = {root:None}
#         def dfs(node):
#             if node:
#                 if node.left:
#                     dic[node.left] = node
#                 if node.right:
#                     dic[node.right] = node
#                 dfs(node.left)
#                 dfs(node.right)
#         dfs(root)
#         l1, l2 = p, q
#         while(l1!=l2):
#             l1 = dic.get(l1, q)
#             l2 = dic.get(l2, p)
#         return l1

# 4 解答成功: 执行耗时:92 ms,击败了56.50% 的Python3用户 内存消耗:28.4 MB,击败了9.52% 的Python3用户
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root:None}
        def dfs(node):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        visited = set()
        while p:
            visited.add(p)
            p = dic[p]
        while q:
            if q in visited:
                return q
            q = dic[q]

# leetcode submit region end(Prohibit modification and deletion)
