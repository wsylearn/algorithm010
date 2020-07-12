学习笔记

# 9 深度优先搜索和广度优先搜索

## 9.1 dfs模板

**递归写法**

```python
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

```python
visited = set() 
def dfs(node, visited):
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

```python
visited = set() 
def dfs(node):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node)  
	# process current node here. 
	...
	dfs(node.left)
    dfs(node.right)
```

**非递归写法**

关键利用了栈stack后进先出的性质

```python
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...
```

## 9.2bfs模板

最短路径问题中，广度优先一般是对的，而深度优先得到的第一个答案还不一定是对的

利用了队列queue的先入先出的性质

```python
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

# 10 贪心算法Greedy

1 希望通过每一步的最优导致全局最优

2 

| 方法     | 描述                         |
| :------- | ---------------------------- |
| 贪心     | 当下做局部最优判断，不能回退 |
| 回溯     | 能够回退                     |
| 动态规划 | 最优判断+能够回退            |

3 最小生成树，霍夫曼编码等使用

4 贪心一般不能求得所要的答案，但是如果可以通过贪心算法解决一般都是最好的办法。一般用来辅助求解，或解决一些要求精度不高的问题。

# 11 二分查找

## 11.1 二分查找前提

1 目标函数单调递增或递减（有序的）

2 存在上下界（bounded）

3 能够通过索引访问（index accessible）（单链表不好用二分查找，除非把单链表改造成跳表等）

## 11.2 二分查找模板

```Python
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```



