# 设计实现双端队列。
# 你的实现需要支持以下操作：
#
#
#  MyCircularDeque(k)：构造函数,双端队列的大小为k。
#  insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
#  insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
#  deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
#  deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
#  getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
#  getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
#  isEmpty()：检查双端队列是否为空。
#  isFull()：检查双端队列是否满了。
#
#
#  示例：
#
#  MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#  
#
#
#
#  提示：
#
#
#  所有值的范围为 [1, 1000]
#  操作次数的范围为 [1, 1000]
#  请不要使用内置的双端队列库。
#
#  Related Topics 设计 队列


# leetcode submit region begin(Prohibit modification and deletion)

# 1 解答成功: 执行耗时:256 ms,击败了7.22% 的Python3用户 内存消耗:14 MB,击败了100.00% 的Python3用户
# class MyCircularDeque:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the deque to be k.
#         """
#         self.queue_right = []
#         self.queue_left = []
#         self.size = k
#
#     def insertFront(self, value: int) -> bool:
#         """
#         Adds an item at the front of Deque. Return true if the operation is successful.
#         """
#         if not self.isFull():
#             while self.queue_right:
#                 self.queue_left.append(self.queue_right.pop())
#             self.queue_left.append(value)
#             return True
#         return False
#
#     def insertLast(self, value: int) -> bool:
#         """
#         Adds an item at the rear of Deque. Return true if the operation is successful.
#         """
#         if not self.isFull():
#             while self.queue_left:
#                 self.queue_right.append(self.queue_left.pop())
#             self.queue_right.append(value)
#             return True
#         return False
#
#     def deleteFront(self) -> bool:
#         """
#         Deletes an item from the front of Deque. Return true if the operation is successful.
#         """
#         if not self.isEmpty():
#             while self.queue_right:
#                 self.queue_left.append(self.queue_right.pop())
#             self.queue_left.pop()
#             return True
#         return False
#
#     def deleteLast(self) -> bool:
#         """
#         Deletes an item from the rear of Deque. Return true if the operation is successful.
#         """
#         if not self.isEmpty():
#             while self.queue_left:
#                 self.queue_right.append(self.queue_left.pop())
#             self.queue_right.pop()
#             return True
#         return False
#
#     def getFront(self) -> int:
#         """
#         Get the front item from the deque.
#         """
#         if not self.isEmpty():
#             while self.queue_right:
#                 self.queue_left.append(self.queue_right.pop())
#             return self.queue_left[-1]
#         return -1
#
#     def getRear(self) -> int:
#         """
#         Get the last item from the deque.
#         """
#         if not self.isEmpty():
#             while self.queue_left:
#                 self.queue_right.append(self.queue_left.pop())
#             return self.queue_right[-1]
#         return -1
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular deque is empty or not.
#         """
#         return not self.queue_right and not self.queue_left
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular deque is full or not.
#         """
#         if len(self.queue_right) == self.size or len(self.queue_left) == self.size:
#             return True
#         return False
#
# 2 解答成功: 执行耗时:80 ms,击败了90.72% 的Python3用户 内存消耗:14 MB,击败了100.00% 的Python3用户
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.queue.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.queue

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.queue) == self.size:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
