# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
#  获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在
# 写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#  进阶:
#
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
#  示例:
#
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
# 1 使用python自带的OrderedDict（不推荐）
# 1.1 解答成功: 执行耗时:208 ms,击败了88.62% 的Python3用户 内存消耗:22.1 MB,击败了50.00% 的Python3用户
# import collections
# class LRUCache():
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.ordered_dict = collections.OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.ordered_dict:
#             return -1
#         self.ordered_dict.move_to_end(key)
#         return self.ordered_dict[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.ordered_dict:
#             self.ordered_dict.move_to_end(key)
#         self.ordered_dict[key] = value
#         if len(self.ordered_dict) > self.capacity:
#             self.ordered_dict.popitem(last=False)

# 1.2 解答成功: 执行耗时:264 ms,击败了38.08% 的Python3用户 内存消耗:22.1 MB,击败了50.00% 的Python3用户
# import collections
# class LRUCache():
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.ordered_dict = collections.OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.ordered_dict:
#             return -1
#         v = self.ordered_dict.pop(key)
#         self.ordered_dict[key] = v
#         return v
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.ordered_dict:
#             self.ordered_dict.pop(key)
#         self.ordered_dict[key] = value
#         if len(self.ordered_dict) > self.capacity:
#             self.ordered_dict.popitem(last=False)

# 1.3 解答成功: 执行耗时:204 ms,击败了92.00% 的Python3用户 内存消耗:21.9 MB,击败了80.77% 的Python3用户
# import collections
# class LRUCache(collections.OrderedDict):
#
#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)

# 2 解答成功: 执行耗时:296 ms,击败了24.08% 的Python3用户 内存消耗:22.7 MB,击败了7.69% 的Python3用户
# O(1), O(capacity)
# 哈希表 + 双向链表
# 哈希表：key:node
# 双向链表: node下的：key:value
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed_node = self.remove_tail()
                self.cache.pop(removed_node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val =value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
