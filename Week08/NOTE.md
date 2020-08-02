学习笔记

# 16 位运算

## 16.1 与、或、非、异或的符号

与 &

或 |

非 ~

异或^

## 16.2 异或特点

不同为1，相同为0

```Python
x ^ 0 = x
x ^ 1s = ~x #1s = -0
x ^ (-x) = 1s # 全1
x ^ x = 0
c = a ^ b => a ^ c = b => b ^ c = a #交换律
a ^ b ^ c = a ^ (b^c) = (a^b)^c # 结合律
```

## 16.3 指定位置的位运算

1 将x最右边的n位清零

```python
x & (~0<<n)
```

2 获取x的第n位的值（0或1）

```Python
(x>>n)&1
```

3 获取x的第n位幂值

```Python
x&(1<<n)
```

4 仅将第n位置为1

```Python
x|(1<<n)
```

5 仅将第n位置为0

```Python
x&(~(1<<n))
```

6 将x最高位值第n位（含）清零

```Python
x&((1<<n)-1)
```

## 14.4 常用位运算

1 判断奇数偶数

```Python
x%2 == 1  =>  (x&1) == 1  
x%2 == 0  =>  (x&1) == 0
```

2 整除

```python
x // 2  =>  x >> 1 #右移一位
#例如
mid = (left + right) // 2 => mid = (left + right) >> 1
```

3 清零最低位的1

```python
x = x & (x-1)
```

4 得到最低位的1

```python
x & -x
```

5 

```python
x & -x => 0
```

# 17 布隆过滤器（bloom filter）和LRU cache

## 17.1 布隆过滤器

1 和字典相比，它只能用于检索一个元素是否在一个集合中，不能存储额外的信息。

2 优点：时间效率和空间效率远远超过一般算法

3 缺点：有一定的误识别率和删除困难（模糊查询）

4 布隆过滤器说有，不一定有。说没有，肯定没有。

5 一般当快速地缓存使用，例如查询数据库之前使用，先判断数据库中是否有，有再去数据库查，没有的话就不去数据库查询了，节省时间。

6 代码实现

```python
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

```java
//Java
public class BloomFilter {
    private static final int DEFAULT_SIZE = 2 << 24;
    private static final int[] seeds = new int[] { 5, 7, 11, 13, 31, 37, 61 };
    private BitSet bits = new BitSet(DEFAULT_SIZE);
    private SimpleHash[] func = new SimpleHash[seeds.length];
    public BloomFilter() {
        for (int i = 0; i < seeds.length; i++) {
            func[i] = new SimpleHash(DEFAULT_SIZE, seeds[i]);
        }
    }
    public void add(String value) {
        for (SimpleHash f : func) {
            bits.set(f.hash(value), true);
        }
    }
    public boolean contains(String value) {
        if (value == null) {
            return false;
        }
        boolean ret = true;
        for (SimpleHash f : func) {
            ret = ret && bits.get(f.hash(value));
        }
        return ret;
    }
    // 内部类，simpleHash
    public static class SimpleHash {
        private int cap;
        private int seed;
        public SimpleHash(int cap, int seed) {
            this.cap = cap;
            this.seed = seed;
        }
        public int hash(String value) {
            int result = 0;
            int len = value.length();
            for (int i = 0; i < len; i++) {
                result = seed * result + value.charAt(i);
            }
            return (cap - 1) & result;
        }
    }
}
```

## 17.2 LRU cache

LRU：最近最少使用 

1 python

```python
# Python 
class LRUCache(object): 
	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity
	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 
	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

2 c++

```c++
//C/C++

struct CacheNode {
    int key, value;
    CacheNode *pre, *next;
      
    CacheNode(int key_ = 0, int value_ = 0) 
        : key(key_), value(value_), pre(NULL), next(NULL) {}
};

class LRUCache {
public:
    LRUCache(int capacity) 
        : _capacity(capacity), _head(new CacheNode()), _tail(_head) {}
    
    int get(int key) {
        auto it = _cache.find(key);
        if (it == _cache.end()) return -1;
        
        moveToTail(it->second);
        return it->second->value;
    }
    
    void put(int key, int value) {
        auto it = _cache.find(key);
        
        if (it != _cache.end()) {
            it->second->value = value;
            moveToTail(it->second);
        }
        else if ((int)_cache.size() < _capacity) {
            auto node = new CacheNode(key, value);
            addToTail(node);          
            _cache[key] = node;
        }
        else {
            // Reuse existing node
            _cache.erase(_head->next->key);
            moveToTail(_head->next);
            _tail->key = key; _tail->value = value;
            _cache[key] = _tail;
        }
    }
    
    ~LRUCache() {
        auto pCurr = _head;
        while (pCurr != NULL) {
            auto next = pCurr->next;
            delete pCurr;
            pCurr = next;
        }
    }
    
private:
    const int _capacity;
    CacheNode *const _head, *_tail;
    unordered_map<int, CacheNode*> _cache;
    
    void moveToTail(CacheNode *node) {
        if (node == _tail) return;
        
        node->pre->next = node->next;
        node->next->pre = node->pre;
        
        addToTail(node);
    }
    
    void addToTail(CacheNode *node) {
        node->next = _tail->next;
        _tail->next = node;
        node->pre = _tail;
        _tail = node;                   
    }
};
```

3 java

```java
/**
 * 使用 哈希表 + 双端链表 实现
 */
class LinkedNode {
  constructor(key = 0, val = 0) {
    this.key = key
    this.val = val
    this.prev = null
    this.next = null
  }
}


class LinkedList {
  constructor() {
    this.head = new LinkedNode()
    this.tail = new LinkedNode()
    this.head.next = this.tail
    this.tail.prev = this.head
  }


  insertFirst(node) {
    node.next = this.head.next
    node.prev = this.head
    this.head.next.prev = node
    this.head.next = node
  }


  remove(node) {
    node.prev.next = node.next
    node.next.prev = node.prev
  }


  removeLast() {
    if (this.tail.prev === this.head) return null
    let last = this.tail.prev
    this.remove(last)
    return last
  }
}


/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  this.capacity = capacity
  this.keyNodeMap = new Map()
  this.cacheLink = new LinkedList()
};


/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  if (!this.keyNodeMap.has(key)) return -1
  let val = this.keyNodeMap.get(key).val
  this.put(key, val)
  return val
};


/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  let size = this.keyNodeMap.size
  if (this.keyNodeMap.has(key)) {
    this.cacheLink.remove(this.keyNodeMap.get(key)); 
    --size 
  }
  if (size >= this.capacity) {
    this.keyNodeMap.delete(this.cacheLink.removeLast().key)
  }
  let node = new LinkedNode(key, value)
  this.keyNodeMap.set(key, node)
  this.cacheLink.insertFirst(node)
};
```

```java
class LRUCache {
    /**
     * 缓存映射表
     */
    private Map<Integer, DLinkNode> cache = new HashMap<>();
    /**
     * 缓存大小
     */
    private int size;
    /**
     * 缓存容量
     */
    private int capacity;
    /**
     * 链表头部和尾部
     */
    private DLinkNode head, tail;

    public LRUCache(int capacity) {
        //初始化缓存大小，容量和头尾节点
        this.size = 0;
        this.capacity = capacity;
        head = new DLinkNode();
        tail = new DLinkNode();
        head.next = tail;
        tail.prev = head;
    }

    /**
     * 获取节点
     * @param key 节点的键
     * @return 返回节点的值
     */
    public int get(int key) {
        DLinkNode node = cache.get(key);
        if (node == null) {
            return -1;
        }
        //移动到链表头部
         (node);
        return node.value;
    }

    /**
     * 添加节点
     * @param key 节点的键
     * @param value 节点的值
     */
    public void put(int key, int value) {
        DLinkNode node = cache.get(key);
        if (node == null) {
            DLinkNode newNode = new DLinkNode(key, value);
            cache.put(key, newNode);
            //添加到链表头部
            addToHead(newNode);
            ++size;
            //如果缓存已满，需要清理尾部节点
            if (size > capacity) {
                DLinkNode tail = removeTail();
                cache.remove(tail.key);
                --size;
            }
        } else {
            node.value = value;
            //移动到链表头部
            moveToHead(node);
        }
    }

    /**
     * 删除尾结点
     *
     * @return 返回删除的节点
     */
    private DLinkNode removeTail() {
        DLinkNode node = tail.prev;
        removeNode(node);
        return node;
    }

    /**
     * 删除节点
     * @param node 需要删除的节点
     */
    private void removeNode(DLinkNode node) {
        node.next.prev = node.prev;
        node.prev.next = node.next;
    }

    /**
     * 把节点添加到链表头部
     *
     * @param node 要添加的节点
     */
    private void addToHead(DLinkNode node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    /**
     * 把节点移动到头部
     * @param node 需要移动的节点
     */
    private void moveToHead(DLinkNode node) {
        removeNode(node);
        addToHead(node);
    }

    /**
     * 链表节点类
     */
    private static class DLinkNode {
        Integer key;
        Integer value;
        DLinkNode prev;
        DLinkNode next;

        DLinkNode() {
        }

        DLinkNode(Integer key, Integer value) {
            this.key = key;
            this.value = value;
        }
    }
}
```

# 18 排序算法

1比较类排序：通过比较来决定元素间相对次序，时间复杂度不能突破nlogn, 成为非线性时间排序。（可以是对象排序，不仅仅是数字排序）

2 非比较类排序：不通过比较来决定元素间相对次序，可以线性时间运行，以此也成为了线性时间非比较类排序。（一般仅仅是数字排序）

3 

![](E:\my_note\09_geek\my_note\note_images\2.png)

## 18.1 普通排序

时间复杂度：$O(n^2)$

### 18.1.1  选择排序 Selection Sort

```Python
# 1
def selection_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                
# 2
def selection_sort2(nums):
    for i in range(len(nums)-1):
        min_val = nums[i]
        min_val_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_val_index = j
        nums[i], nums[min_val_index] = nums[min_val_index], nums[i]
        
selection_sort(nums)
```

### 18.1.2 插入排序 Insertion Sort

```python
# 1
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j > 0 and nums[i] < nums[j]:
            j -= 1
        nums.insert(j+1, nums.pop(i))
        
# 2
def insertion_sort2(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
```

### 18.1.3 冒泡排序 Bubble Sort

```python
# 1
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
# 2
def bubble_sort2(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
```



## 18.2 高级排序

时间复杂度$O(nlogn)$

### 18.2.1 快排

分治的思想

O（nlogn）：主定理可以推出时间复杂度

```python
#Python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark

# 调用方式
quick_sort(0, len(nums)-1, nums)
```

### 18.2.2 归并排序（merge sort）

分治思想

```python
def merge_sort(array, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1 # mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid+1, right)
    merge(array, left, mid, right)


def merge(array, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    if i <= mid:
        temp += array[i:mid + 1]
    else:
        temp += array[j:right + 1]
    array[left:right + 1] = temp
```

```python
def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)

def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1,4]
print '排序前：',seq
result = mergesort(seq)
print '排序后：',result
```

### 18.2.3 堆排序 Heap Sort

堆插入O（logn）,取最小值或最大值O(1)

1 数组元素依次插入建立小顶堆

2 依次取出堆顶元素并删除

```python
import heapq
def heap_sort(array):
    pq = []
    n = len(array)
    for i in range(n):
        heapq.heappush(pq, array[i])
    for i in range(n):
        array[i] = heapq.heappop(pq)
```

```python
# 更快，线性时间
import heapq
def heap_sort(array):
    pq = array.copy()
    heapq.heapify(pq)
    for i in range(len(array)):
        array[i] = heapq.heappop(pq)
```

```python
#Python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp

def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```

## 18.3 特殊排序

时间复杂度: $O(n)$

特殊排序不是重点

### 18.3.1 计数排序

1元素必须是整数

2 元素值不能太大

### 18.3.2 桶排序

计数排序的升级版

### 18.3.3 基数排序

 只能排整型数

