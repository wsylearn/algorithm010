学习笔记

# 6 图  

树没有环，图有环

可以这么认为：链表是特殊化的树，树是特殊化的图

单链表增删为O（n），但查询为为O（n）

二叉搜索树的查询为O（logn），不在是O（n），相当于加速了，其他操作也是O（logn）

https://visualgo.net/en

二叉堆的大顶堆：

find-max: O(1)

delete-max: O(logN)

insert(create): O(logN) or O(1)

二叉堆只是一种常见且简单实现的堆，但并不是最优的实现。实际工程并不使用二叉堆，而是直接使用优先队列（priority queue）（Python中的heapq库）

树中，可以不写visited=set（），但是图中必须要写

二叉搜索树的中序遍历是递增的

# 7 泛型递归、树的递归

## 7.1 递归模板

归去来兮

```python
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

## 7.2 递归步骤

1 recursion terminator 终结条件

2 process logic in current level  处理这一层

3 drill down 进入下一层

4 reverse the current level status if needed 如果需要的话，清理本层变量

## 7.3 思维要点

1 抵制人肉递归

2 找最近重复性

3 数学归纳法思维

# 8 分治（divide）、回溯（conquer）

## 8.1 分治

1 分治和回溯是一种特殊的、复杂的递归

2 找重复性（分解（split）成子问题）

​	最近重复性

​	最优重复性：动态规划

3 分治与泛型递归最大的不同是，分治要把得到的子的结果进行组合合并（merge）

4 分治代码模板

```python
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

## 8.2 回溯

采用试错的思想

不断的再每一层去尝试，典型应用：八皇后，数独，括号生成（尽早判断括号合不合法）

