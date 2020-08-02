# 给出一个区间的集合，请合并所有重叠的区间。
#
#  示例 1:
#
#  输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2:
#
#  输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#  Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:40 ms,击败了98.16% 的Python3用户 内存消耗:14.4 MB,击败了91.75% 的Python3用户
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                if right < intervals[i][1]:
                    right = intervals[i][1]
            else:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        res.append([left, right])
        return res
# leetcode submit region end(Prohibit modification and deletion)
a = [1,2,3,4]
sorted()