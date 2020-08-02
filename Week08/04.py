# 给你两个数组，arr1 和 arr2，
#
#
#  arr2 中的元素各不相同
#  arr2 中的每个元素都出现在 arr1 中
#
#
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。
#
#
#
#  示例：
#
#  输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
#
#
#
#  提示：
#
#
#  arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000
#  arr2 中的元素 arr2[i] 各不相同
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中
#
#  Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:64 ms,击败了21.92% 的Python3用户 内存消耗:13.8 MB,击败了43.75% 的Python3用户
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         in_arr2 = []
#         not_in_arr2 = []
#         counter = {}
#         for i in arr1:
#             counter[i] = counter.get(i, 0) + 1
#         arr1 = set(arr1)
#         arr2_ = set(arr2.copy())
#         for i in arr1:
#             if i not in arr2_:
#                 not_in_arr2 += [i]*counter[i]
#         not_in_arr2.sort()
#         for j in arr2:
#             in_arr2 += [j]*counter[j]
#         return in_arr2 + not_in_arr2

# 2 解答成功: 执行耗时:48 ms,击败了80.87% 的Python3用户 内存消耗:13.7 MB,击败了62.50% 的Python3用户
# 计数排序
# from collections import Counter
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         count = Counter(arr1)
#         i = 0
#         for num2 in arr2:
#             c = count[num2]
#             count.pop(num2)
#             arr1[i:i+c] = [num2] * c
#             i += c
#
#         tmp = []
#         for num1 in count:
#             tmp += [num1] * count[num1]
#         tmp.sort()
#         arr1[i:] = tmp
#         return arr1


# 3 # 解答成功: 执行耗时:44 ms,击败了93.36% 的Python3用户 内存消耗:13.7 MB,击败了75.00% 的Python3用户
# 自定义比较函数
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         num2index = {arr2[i]:i for i in range(len(arr2))}
#         def sort_fun(n):
#             return num2index.get(n, n+1000)
#         arr1.sort(key=sort_fun)
#         return arr1

# 4 解答成功: 执行耗时:56 ms,击败了45.68% 的Python3用户 内存消耗:13.8 MB,击败了34.38% 的Python3用户
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = []
        for i in arr1[:]:
            if i not in arr2:
                x.append(i)
                arr1.remove(i)

        x.sort()
        arr1.sort(key=lambda x: arr2.index(x))
        return arr1 + x

# leetcode submit region end(Prohibit modification and deletion)
