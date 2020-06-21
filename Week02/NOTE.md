学习笔记

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