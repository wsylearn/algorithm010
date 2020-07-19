学习笔记

# 12 动态规划

## 12.1 动态规划知识点

1 将复杂问题分解为子问题，寻找重复性

2 分治、回溯、递归、动态规划等没有本质区别

3 数学归纳法

4 本质：寻找重复性 

5 DP关键点：

​	1）动态规划和递归或者分治没有根本上的区别，关键看有无最优子结构

​	2） 共性：找到重复子问题

​	3）差异性：最优子结构、中途可以淘汰次优解（不淘汰的话会是指数级的时间复杂度，淘汰的话一般会变成n^2,或n）

6 麻省理工教程、算法导论、大学课本

## 12.2 递归代码模板

```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```



```java
// Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}
```

## 12.3 分治代码模板

```Python
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```





































