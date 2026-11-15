---
rank: 2
id: "146"
title: LRU缓存机制
difficulty: 中等
tags: [设计, 哈希表, 链表]
freq: 969
link: https://leetcode.cn/problems/lru-cache/
desc: 实现 get / put 都是 O(1) 的 LRU 缓存，超出容量时淘汰最久未使用的 key。
---
## 思路

- **哈希表 + 双向链表**：哈希表 O(1) 找节点，双向链表维护使用顺序。
- 约定：**刚访问的放尾部，头部永远是最久未用的**，淘汰时删头。
- `get`：存在就挪到尾部。`put`：已存在则更新并挪到尾部；不存在则插到尾部，超容量删头。
- 写法一直接用语言自带的有序哈希表；面试官说「不能用库」时写写法二。

## 易错点

- 手写链表时节点要存 `key`：淘汰头节点时还得用它去删哈希表。
- 用两个哨兵 `head` / `tail`，`remove`、`addLast` 就不用判空。
- `put` 已存在的 key 也算一次访问，要挪到尾部。

## 代码

### 写法一：LinkedHashMap / OrderedDict

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()             # 头部最久未用，尾部最近使用

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)     # 弹出头部
```

```java
class LRUCache {
    private final int cap;
    private final LinkedHashMap<Integer, Integer> map = new LinkedHashMap<>();   // 头部最久未用，尾部最近使用

    public LRUCache(int capacity) {
        cap = capacity;
    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        int val = map.remove(key);             // 删掉再放回尾部 = 标记为最近使用
        map.put(key, val);
        return val;
    }

    public void put(int key, int value) {
        map.remove(key);
        map.put(key, value);
        if (map.size() > cap) {
            map.remove(map.keySet().iterator().next());   // 第一个 key 就是最久未用
        }
    }
}
```

### 写法二：手写双向链表

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}                          # key -> Node
        self.head, self.tail = Node(), Node()  # 哨兵：head 后面最久未用，tail 前面最近使用
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_last(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
        else:
            if len(self.map) == self.cap:
                old = self.head.next
                self._remove(old)
                del self.map[old.key]
            node = Node(key, value)
            self.map[key] = node
        self._add_last(node)
```

```java
class LRUCache {
    private static class Node {
        int key, val;
        Node prev, next;
        Node(int key, int val) { this.key = key; this.val = val; }
    }

    private final int cap;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0);   // 哨兵：head 后面最久未用，tail 前面最近使用

    public LRUCache(int capacity) {
        cap = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node node = map.get(key);
        if (node == null) return -1;
        remove(node);
        addLast(node);
        return node.val;
    }

    public void put(int key, int value) {
        Node node = map.get(key);
        if (node != null) {
            node.val = value;
            remove(node);
        } else {
            if (map.size() == cap) {
                Node old = head.next;
                remove(old);
                map.remove(old.key);
            }
            node = new Node(key, value);
            map.put(key, node);
        }
        addLast(node);
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addLast(Node node) {
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
    }
}
```

**复杂度**：`get` / `put` 均 O(1)，空间 O(capacity)。
