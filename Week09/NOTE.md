学习笔记

# 19 高级动态规划

## 19.1 复习

### 19.1.1 递归

函数自己调用自己

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 1 递归终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 2 处理本层逻辑
    process(level, data...) 
    # drill down 3 下到下一层
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 4 如果需要的话，清除本层的变量
```

### 19.1.2 分治

分而治之（例如归并排序）

```Python
![3](E:\my_note\09_geek\my_note\note_images\3.png)# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 1 递归终止条件
  if problem is None: 
	print_result 
	return 
  # prepare data 2 准备数据和拆分问题
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 3 对子问题调分治函数递归求解
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 4 合并结果
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states 5 清除本层状态变量
```

![](E:\my_note\09_geek\my_note\note_images\3.png)

### 19.1.3 回溯

### 19.1.4 动态规划

分治+最优子结构+动态递推

动态规划和递归或者分治没有根本的区别（关键看有无最优子结构)

共性：都是找到重复子问题

差异性：动态规划是找到最优子结构，中途可以淘汰次优解

难点：状态转移方程

例如：

​	1 斐波那契数列：f(n) = f(n-1) + f(n-2)

​	2 路径问题：f(x,y) = f(x-1, y) + f(x, y-1)

​	3 

## 19.2 思维

1 人肉递归低效，很累

2 找到最近最简方法，将其拆解成可重复性解决的问题

3 数学归纳法的思维

## 19.3 复杂的原因

1 状态的维度更多了（二维，三维，或更多，甚至需要压缩）

2 状态方程更加复杂

## 19.4 进阶版爬楼梯

1 若每次能为1，2，3，则结果？（easy）

```python
# 1.1
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         if n == 3:
#             return 4
#         f1, f2, f3 = 1, 2, 4
#         for i in range(4, n+1):
#             f = f1 + f2 + f3
#             f1, f2, f3 = f2, f3, f
#         return f3

# 1.2 7040ms
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def helper(n):
#             if n <= 2:
#                 return n
#             if n == 3:
#                 return 4
#             return helper(n-1) + helper(n-2) + helper(n-3)
#         return helper(n)

# 1.3 0ms
# from functools import lru_cache
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         @lru_cache(None)
#         def helper(n):
#             if n <= 2:
#                 return n
#             if n == 3:
#                 return 4
#             return helper(n-1) + helper(n-2) + helper(n-3)
#         return helper(n)
#
# print(Solution().climbStairs(1))
# print(Solution().climbStairs(2))
# print(Solution().climbStairs(3))
# print(Solution().climbStairs(4))
# print(Solution().climbStairs(5))
# print(Solution().climbStairs(30))
# 1， 2， 4， 7， 13， 53798080
```

2 若每次步长为steps里，则结果？（类似硬518. 零钱兑换 II）

```python
# 2.1
# DP
# from typing import List
# class Solution:
#     def climbStairs(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount+1)
#         dp[0] = 1
#         for i in range(1, amount+1):
#             for c in coins:
#                 if i - c >= 0:
#                     dp[i] += dp[i - c]
#         return dp[-1]

# 2.2
# 递归
# from typing import List
# from functools import lru_cache
# class Solution:
#     def climbStairs(self, amount: int, coins: List[int]) -> int:
#         @lru_cache(None)
#         def helper(n):
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return 1
#             return sum(helper(n-c) for c in coins)
#
#         return helper(amount)

# print(Solution().climbStairs(1, [1,2,3]))
# print(Solution().climbStairs(2, [1,2,3]))
# print(Solution().climbStairs(3, [1,2,3]))
# print(Solution().climbStairs(4, [1,2,3]))
# print(Solution().climbStairs(5, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,5]))
# 1， 2， 4， 7， 13， 53798080, 5508222
```

#3 若相邻两步的步伐不能一样，则结果如何？（mid）

```python
# 3 dp
from typing import List
# class Solution:
#     def climbStairs(self, amount: int, steps: List[int]) -> int:
#         dp = [[0]*len(steps) for _ in range(amount+1)]
#         for i in range(1, amount+1):
#             for j in range(len(steps)):
#                 if i == steps[j]:
#                     dp[i][j] = 1
#                 elif i - steps[j] > 0:
#                     for k in range(len(steps)):
#                         if k != j:
#                             dp[i][j] += dp[i - steps[j]][k]
#         return sum(dp[-1])

# 循环
# dp[i][j]表示走到i步，且到这步走了steps[j]步
# 那么dp[i][j] = sum(dp[i - steps[j]][k]) k != j
# 起始条件是
# dp[steps[j]][j] = 1, j从0到ns - 1
# dp[负数][j] = 0
# class Solution:
#     def climbStairs(self, n: int, steps: List[int]) -> int:
#         ns = len(steps)
#         dp = [[0 for _ in range(ns)] for _ in range(n + 1)]
#
#         for i in range(n + 1):
#             for j in range(ns):
#                 if i == steps[j]:
#                     dp[i][j] = 1
#                 else:
#                     res = 0
#                     for k in range(ns):
#                         if k != j and i >= steps[j]:
#                             res += dp[i - steps[j]][k]
#                     dp[i][j] = res
#                     # dp[i][j] = sum(dp[i - steps[j]][k] for k in range(ns) if k != j and i >= steps[j])
#         return sum(dp[n])

# print(Solution().climbStairs(1, [1,2,3]))
# print(Solution().climbStairs(2, [1,2,3]))
# print(Solution().climbStairs(3, [1,2,3]))
# print(Solution().climbStairs(4, [1,2,3]))
# print(Solution().climbStairs(5, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,5]))
# # 1, 1, 3, 3, 4, 32103, 2487
```

# 20 字符串算法

## 20.1 字符串immutable

Python中的字段串是不可变（immutable）类型

## 20.2 atoi模板

(表示ascii to integer)是把字符串转换成整型数的一个函数

```Python
# Python
class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
```

## 20.3 常见字符串题目

经常字符串和动态规划相结合

**最长子串，子序列问题**

子序列可以有间隔，子串不能有间隔

1 最长子序列（NO.1143）

```python
if text1[i - 1] == text2[j - 1]:  # 不是 text1[i] == text2[j]
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
return dp[-1][-1]
```

2 最长子串

```python
if text1[i - 1] == text2[j - 1]:  # 不是 text1[i] == text2[j]
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = 0
# 最后再所有的值中找最大值，而不是最后的值
```

3 编辑距离（NO.72）

```python
if text1[i - 1] == text2[j - 1]: 
    dp[i][j] = dp[i - 1][j - 1]
else:
    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j])
return dp[-1][-1]
```

4 最长回文子串（NO.5）

```python
# P(i, j)代表s[i:j+1]是不是回文串（注意，i，j都是索引）
#if s[i] == s[j] and dp[i+1][j-1]:
if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
    dp[i][j] = True
else:
    dp[i][j] = False
```

5 通配符匹配问题（NO.10）

​	加缓存memo

```python
pre = bool(s) and p[0] in {s[0], "."}
if len(p) >= 2 and p[1] == "*":
    return self.isMatch(s, p[2:]) or (pre and self.isMatch(s[1:], p)) # * 匹配0次或多次
else:
    return pre and self.isMatch(s[1:], p[1:])
```

```python
pre = i < len_s and p[j] in {s[i], "."}
if j + 1 <= len_p - 1 and p[j + 1] == "*":
    ans = dp(i, j + 2) or (pre and dp(i + 1, j))
else:
    ans = pre and dp(i + 1, j + 1)
memo[(i, j)] = ans
```

```python
# 斐波那契数列和本问题的对比
def fib(n):
    fib(n - 1) #1
    fib(n - 2) #2
    
def dp(i, j):
    dp(i, j + 2)     #1 * 匹配0次
    dp(i + 1, j)     #2 * 匹配1次
    dp(i + 1, j + 1) #3 没有*
```

6 不同的子序列(NO.115)

```python
# s是原料，可以不用完，t是目标，必须达成
#dp[i][j]代表t[:i]能用s[:j]来组成的个数
if t[i - 1] == s[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
else:
    dp[i][j] = dp[i][j - 1]
return dp[-1][-1] 
```

## 20.4 字符串匹配算法

### 1 暴力法（brute force）

O（mn）,m和n分别为两个字符串的长度

```python
def force_search(txt, pat):
    m, n = len(txt), len(pat)
    for i in range(m-n):
        for j in range(n):
            if txt[i+j] != pat[j]:
                break
        else:
            return i
    return -1

print(force_search("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
```

### 2 rabin-karp算法

比较txt[i:i+n]的哈希值与pat的哈希值是否相等，如果相等再暴力一个一个字母比较，如果不等直接i加1

```python
# O(mn)
def rabin_karp_search(txt, pat):
    m, n = len(txt), len(pat)
    hash_pat = hash(pat)
    for i in range(m-n):
        if hash(txt[i:i+n]) != hash_pat:
            continue
        for j in range(n):
            if txt[i+j] != pat[j]:
                break
        else:
            return i
    return -1

# def rabin_karp_search(txt, pat):
#     m, n = len(txt), len(pat)
#     set_pat = set(pat)
#     for i in range(m-n):
#         if set(txt[i:i+n]) != set_pat:
#             continue
#         for j in range(n):
#             if txt[i+j] != pat[j]:
#                 break
#         else:
#             return i
#     return -1
```

**通过滑动窗口来加速**

O(m)

```python
# 老师给的
#Python
class Solution:
    def strStr(self, txt: str, pat: str) -> int:
        M, N = len(txt), len(pat)
        if N > M:
            return -1

        Q = 9997 # 是素数就行,例如99197
        higest_pow = pow(256, N-1) % Q # 最高位权重
        txt_hash = pat_hash = 0
        for i in range(N): # preprocessing
            txt_hash = (256 * txt_hash + ord(pat[i])) % Q
            pat_hash = (256 * pat_hash + ord(txt[i])) % Q
        for i in range(M-N+1): # note the +1
            if txt_hash == pat_hash: # check character by character
                for j in range(N):
                    if pat[j] != txt[i + j]:
                        break
                else:
                    return i
            if i < M-N:
                pat_hash = (pat_hash - higest_pow * ord(txt[i])) % Q
                pat_hash = (pat_hash * 256 + ord(txt[i + N])) % Q
                pat_hash = (pat_hash + Q) % Q # 防止出现负数（例如-3%7）
        return -1
```

### 3 KMP算法

 找已经匹配的地方的最前面和最后索引，下次直接移到下一个

### 4 Boyer-Moore算法

### 5 sunday算法