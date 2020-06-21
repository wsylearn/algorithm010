# 我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#
#
#  示例:
#
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#
#  1 是丑数。
#  n 不超过1690。
#
#
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:964 ms,击败了5.03% 的Python3用户 内存消耗:13.6 MB,击败了100.00% 的Python3用户
from queue import PriorityQueue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 集合+优先队列
        pq = PriorityQueue()
        rec = set()

        pq.put(1)
        rec.add(1)

        i = 1
        while True:
            x = pq.get()
            if i == n:
                return x
            i+=1
            for k in 2*x, 3*x, 5*x:
                if k not in rec:
                    rec.add(k)
                    pq.put(k)

        return -1

# leetcode submit region end(Prohibit modification and deletion)
