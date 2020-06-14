# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。
#
#  示例:
#
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#  Related Topics 栈 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# 1 暴力求解，超时了
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         for i in range(len(height)):
#             max_left, max_right = 0, 0
#             for j in range(i-1, -1, -1):
#                 max_left = max(max_left, height[j])
#             for j in range(i+1, len(height)):
#                 max_right = max(max_right, height[j])
#             res += max(min(max_left, max_right) - height[i], 0)
#         return res

# 2 解答成功: 执行耗时:48 ms,击败了73.68% 的Python3用户 内存消耗:14.1 MB,击败了8.00% 的Python3用户
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)

        left,right = 0, n - 1  # 分别位于输入数组的两端
        maxleft,maxright = height[0],height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
