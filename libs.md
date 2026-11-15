# 算法常用库速查

刷题时反复用到的标准库，按语言分两栏。每一节末尾会自动列出本仓库里用到它的题目。

LeetCode 的 Python 环境已经预先 `from collections import *`、`from heapq import *`、`from bisect import *`、`from functools import *`、`from math import *`、`import random` 等，所以笔记里的代码都省略了 import；本地运行时需要自己补上。Java 环境预先 `import java.util.*`。

## Python

### `deque` — 双端队列（队列 / BFS / 单调队列）
<!-- match: \bdeque\b -->

两端进出都是 O(1)。`list.pop(0)` 是 O(n)，所以队列一律用 `deque`。

```python
from collections import deque

q = deque()                # 也可以 deque([root])、deque(iterable)
q.append(x)                # 右端进
q.appendleft(x)            # 左端进
q.pop()                    # 右端出
q.popleft()                # 左端出
q[0], q[-1]                # 看两端，不弹出
len(q)                     # 判空直接 while q:
```

- BFS 模板：`q = deque([root])`，循环里 `for _ in range(len(q))` 处理一整层（`range` 的长度在进入循环时就定了）。
- 单调队列：队尾 `pop()` 维护单调性，队头 `popleft()` 淘汰过期元素。
- 可以放 `None`（Java 的 `ArrayDeque` 不行）。
- 按下标访问中间元素是 O(n)，不要当数组用。

### `heapq` — 堆（优先队列）
<!-- match: \b(heapq|heappush|heappop|heapify)\b -->

对一个普通 `list` 做堆操作，**只有小顶堆**。

```python
import heapq

h = []
heapq.heappush(h, x)       # 入堆 O(log n)
x = heapq.heappop(h)       # 弹出最小值 O(log n)
h[0]                       # 看最小值，不弹出
heapq.heapify(nums)        # 原地建堆 O(n)
heapq.heapreplace(h, x)    # 先弹出最小值再压入 x，比分开写快
heapq.heappushpop(h, x)    # 先压入 x 再弹出最小值
heapq.nlargest(k, nums)    # 最大的 k 个；nsmallest 同理
```

- 大顶堆：存相反数，`heappush(h, -x)`，取出来再取反。
- 堆里放元组时按字典序比较：`(优先级, 序号, 对象)`。中间加一个唯一的序号，优先级相同时就不会去比较后面那个不可比的对象（如 `ListNode`）。
- 「第 k 大」：维护一个大小为 k 的**小**顶堆，堆顶就是答案。
- 堆只保证 `h[0]` 最小，整个列表并不是有序的。

### `defaultdict` / `Counter` — 计数与分组
<!-- match: \b(defaultdict|Counter)\b -->

```python
from collections import defaultdict, Counter

cnt = defaultdict(int)     # 不存在的 key 默认是 0
cnt[x] += 1
graph = defaultdict(list)  # 默认是空列表，建图 / 分组
graph[u].append(v)

c = Counter("abca")        # {'a': 2, 'b': 1, 'c': 1}
c["z"]                     # 不存在返回 0，不报错
c.most_common(2)           # 出现最多的 2 个：[('a', 2), ('b', 1)]
Counter(s) == Counter(t)   # 判断是否是字母异位词
```

- `defaultdict` **读取**不存在的 key 也会把它插进去（`if d[k]` 会让字典变大）；只想判断存在用 `k in d`。
- `Counter` 读取不存在的 key 返回 0 且不会插入；`len(c)` 是不同元素的个数。
- 普通字典的等价写法：`d[x] = d.get(x, 0) + 1`。

### `OrderedDict` — 记住顺序的字典
<!-- match: \bOrderedDict\b -->

LRU 这类「既要 O(1) 查找、又要维护先后顺序」的场景。

```python
from collections import OrderedDict

od = OrderedDict()
od[k] = v                  # 新 key 放在末尾；已有的 key 只改值、位置不变
od.move_to_end(k)          # 挪到末尾（最近使用）
od.move_to_end(k, last=False)   # 挪到开头
od.popitem(last=False)     # 弹出开头（最久未用），返回 (k, v)
od.popitem()               # 弹出末尾
next(iter(od))             # 看第一个 key
```

- Python 3.7+ 普通 `dict` 也保持插入顺序，但没有 `move_to_end`，`popitem()` 也只能弹末尾。

### `bisect` — 二分查找
<!-- match: \bbisect(_left|_right)?\b -->

在**已排序**的列表上二分，返回插入位置。

```python
from bisect import bisect_left, bisect_right

i = bisect_left(a, x)      # 第一个 >= x 的位置（lower_bound）
j = bisect_right(a, x)     # 第一个 >  x 的位置（upper_bound）
j - i                      # x 出现的次数
bisect_left(a, x, lo, hi)  # 只在 a[lo:hi] 里找
```

- 判断 `x` 是否存在：`i < len(a) and a[i] == x`。
- 最后一个 `<= x` 的位置是 `bisect_right(a, x) - 1`；最后一个 `< x` 的位置是 `bisect_left(a, x) - 1`。
- 3.10+ 支持 `key=` 参数。
- 面试让手写时，对应的模板见 [34](#/34)、[704](#/704)。

### 排序：`sort` / `sorted` / `cmp_to_key`
<!-- match: \.sort\(|\bsorted\(|\bcmp_to_key\b -->

```python
nums.sort()                            # 原地排序，返回 None
b = sorted(nums)                       # 返回新列表，可以排任意可迭代对象
nums.sort(reverse=True)                # 降序
intervals.sort(key=lambda x: x[0])     # 按某个字段
people.sort(key=lambda p: (-p[0], p[1]))   # 多关键字：第一个降序、第二个升序

from functools import cmp_to_key
strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))   # 自定义两两比较
```

- 排序是稳定的（Timsort），相等的元素保持原来的相对顺序。
- `cmp` 函数返回负数表示 `a` 排前面，对应 Java 比较器 `(a, b) -> ...` 的返回值。
- `x = nums.sort()` 得到的是 `None`，常见手误。

### `@cache` — 记忆化
<!-- match: @cache|\blru_cache\b -->

给递归函数加一行装饰器，就是自顶向下的 DP。

```python
from functools import cache            # 3.9+；老版本用 lru_cache(None)

@cache
def dp(i, j):
    if i == 0:
        return 1
    return dp(i - 1, j) + dp(i, j - 1)
```

- 参数必须可哈希：传下标、元组，不要传 `list`。
- 状态只放在参数里，函数体不要依赖会变化的外部变量。
- 递归太深会栈溢出，见下面「递归」一节。

### `inf`、`divmod` — 无穷大与取整
<!-- match: \binf\b|\bdivmod\b -->

```python
from math import inf       # 等价于 float("inf")
res = inf                  # 求最小值时的初始值；-inf 用于求最大值

carry, digit = divmod(s, 10)   # 同时拿到商和余数

7 // 2      # 3
-7 // 2     # -4   向下取整
int(-7 / 2) # -3   向零取整（C / Java 的行为）
-7 % 2      # 1    余数符号跟除数走；Java 里是 -1
```

- Python 整数不会溢出；题目要求 32 位截断时自己夹一下：`max(-2**31, min(x, 2**31 - 1))`。
- `inf` 是浮点数，只用来比较，不要参与最后的整数结果。

### 列表、切片与常用内置函数

```python
stack = []                 # 列表直接当栈
stack.append(x); stack.pop(); stack[-1]

dp = [0] * n
grid = [[0] * n for _ in range(m)]     # 二维数组；不要写 [[0] * n] * m（每行是同一个对象）

a[::-1]                    # 反转（新列表）
a[i:j]                     # 左闭右开，拷贝
path[:]                    # 浅拷贝，回溯收集答案时用
a[i], a[j] = a[j], a[i]    # 交换

for i, x in enumerate(nums): ...
for x, y in zip(a, b): ...
for i in range(n - 1, -1, -1): ...     # 倒序
max(nums), min(a, b), sum(nums), abs(x)
any(...), all(...)
```

- 交换时两边如果有互相依赖的下标（`nums[i], nums[nums[i] - 1] = ...`），先把下标存到变量里再换。

### 字符串常用操作

```python
s.split()                  # 按任意空白切分，自动去掉多余空格
s.split(".")               # 按指定分隔符
" ".join(words)            # 拼接；循环里用 += 拼长字符串是 O(n²)
s.strip()                  # 去首尾空白；lstrip("0") 去前导 0
s[::-1]                    # 反转
c.isdigit(), c.isalpha(), c.isalnum()
ord("a"), chr(97)          # 字符 <-> 编码；ord(c) - ord("a") 得到 0~25
int("042"), str(42)
s.startswith(p), s.find(p) # find 找不到返回 -1
```

- 字符串不可变：要改字符先 `list(s)`，改完再 `"".join(...)`。

### `random` — 随机数
<!-- match: \brandom\. -->

```python
import random

random.randint(lo, hi)     # [lo, hi] 两端都包含
random.randrange(n)        # [0, n)
random.choice(nums)
random.shuffle(nums)       # 原地打乱
```

- 快排 / 快速选择随机选 pivot 用 `randint(lo, hi)`，注意它是闭区间。

### 递归：`nonlocal` 与递归深度
<!-- match: \bnonlocal\b -->

```python
def solve(root):
    res = 0

    def dfs(node):
        nonlocal res       # 内层函数要给外层变量重新赋值，必须声明
        ...
        res = max(res, x)

    dfs(root)
    return res
```

- 只是调用方法修改对象（`res.append(x)`、`path.pop()`）不需要 `nonlocal`；重新赋值（`res = ...`、`res += 1`）才需要。
- 默认递归深度上限约 1000。本地跑深递归要 `sys.setrecursionlimit(10**6)`；网格 DFS、长链表递归容易踩到，可以改成 BFS / 迭代。

## Java

### `ArrayDeque` — 栈 / 队列 / 双端队列
<!-- match: \bArrayDeque\b -->

一个类顶三个用。栈不要用 `Stack`（继承自 `Vector`，带同步，慢）。

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(x);      // 压栈
stack.pop();        // 弹栈，空了抛异常
stack.peek();       // 看栈顶，空了返回 null

Deque<Integer> q = new ArrayDeque<>();
q.offer(x);         // 入队（队尾）
q.poll();           // 出队（队头），空了返回 null
q.peek();           // 看队头

// 双端：单调队列、滑动窗口
q.offerFirst(x); q.offerLast(x);
q.pollFirst();   q.pollLast();
q.peekFirst();   q.peekLast();

q.isEmpty(); q.size();
```

- **不能放 `null`**（会抛 NPE）。需要把 null 入队时（如 [101](#/101) 的迭代写法）用 `LinkedList`。
- `push / pop / peek` 都在队头操作，`offer` 在队尾加——同一个对象不要混着当栈和队列用。
- `poll()` / `peek()` 空时返回 `null`，直接赋给 `int` 会 NPE，先判 `isEmpty()`。
- BFS 一层：先 `int sz = q.size()` 再循环，循环里队列长度会变。
- 两个栈顶比较时是 `Integer` 对象，用 `equals` 或先拆箱成 `int`。

### `LinkedList` — 链表 / 能放 null 的队列
<!-- match: \bLinkedList\b -->

同时实现了 `List` 和 `Deque`。

```java
LinkedList<Integer> path = new LinkedList<>();
path.add(x);  path.addLast(x);  path.addFirst(x);
path.removeLast();  path.removeFirst();
path.getLast();     path.getFirst();

Queue<TreeNode> q = new LinkedList<>();   // 需要放 null 的队列
```

- 回溯里的 `path` 声明成 `LinkedList` 才有 `removeLast()`；声明成 `List` 的话（Java 21 之前）只能 `path.remove(path.size() - 1)`。
- `get(i)` 是 O(n)，要按下标访问用 `ArrayList`。
- 收集答案时拷贝：`res.add(new ArrayList<>(path))`。
- 当普通队列 / 栈用时，`ArrayDeque` 更快。

### `PriorityQueue` — 堆
<!-- match: \bPriorityQueue\b -->

默认是小顶堆，传比较器改变顺序。

```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);          // 按数组第一个元素
PriorityQueue<ListNode> pq2 = new PriorityQueue<>((a, b) -> a.val - b.val);    // 按节点值

pq.offer(x);        // 入堆 O(log n)
pq.poll();          // 弹出堆顶 O(log n)
pq.peek();          // 看堆顶
pq.size(); pq.isEmpty();
```

- 比较器 `(a, b) -> a - b` 是升序（小顶堆），`b - a` 是降序（大顶堆）。数值可能很大时减法会溢出，用 `Integer.compare(a, b)`。
- 「第 k 大」：大小为 k 的小顶堆，`size() > k` 就 `poll()`，最后 `peek()`。
- 遍历 `PriorityQueue` 不是有序的，只有不断 `poll()` 才有序。
- `remove(Object)` 是 O(n)。

### `HashMap` / `HashSet` — 哈希表
<!-- match: \b(HashMap|HashSet)\b -->

```java
Map<Integer, Integer> map = new HashMap<>();
map.put(k, v);
map.get(k);                              // 不存在返回 null
map.containsKey(k);
map.remove(k);
map.getOrDefault(k, 0);
map.put(k, map.getOrDefault(k, 0) + 1);  // 计数
map.merge(k, 1, Integer::sum);           // 计数的另一种写法
map.putIfAbsent(k, v);
map.computeIfAbsent(k, x -> new ArrayList<>()).add(v);   // 分组 / 建图

for (Map.Entry<Integer, Integer> e : map.entrySet()) { e.getKey(); e.getValue(); }
for (int key : map.keySet()) { }
for (int val : map.values()) { }

Set<Integer> set = new HashSet<>();
set.add(x);          // 已存在返回 false
set.contains(x);
set.remove(x);
```

- **`Integer` 之间比较用 `equals`**：`map.get(a) == map.get(b)` 比的是引用，只有 -128~127 走缓存碰巧相等（[76](#/76) 的经典坑）。和 `int` 字面量或 `int` 变量比较会自动拆箱，没问题。
- `map.get(k)` 返回 `null` 时赋给 `int` 会 NPE，先 `containsKey` 或用 `getOrDefault`。
- key 是字符时类型写 `Character`；字符集固定时（26 个字母、ASCII）直接用 `int[26]` / `int[128]` 更快。
- 遍历顺序不确定；需要顺序用 `LinkedHashMap` / `TreeMap`。

### `LinkedHashMap` — 记住插入顺序的哈希表
<!-- match: \bLinkedHashMap\b -->

哈希表 + 双向链表，LRU 的现成实现。

```java
LinkedHashMap<Integer, Integer> map = new LinkedHashMap<>();
map.put(k, v);                               // 新 key 接在末尾；已有 key 只改值、位置不变
int oldest = map.keySet().iterator().next(); // 第一个（最早插入的）key
map.remove(k);

new LinkedHashMap<>(16, 0.75f, true);        // 第三个参数 true：按访问顺序，get 之后自动挪到末尾
```

- 默认按插入顺序，「访问后挪到末尾」要自己 `remove` 再 `put`，或者用上面三个参数的构造函数。
- 面试写 LRU 通常要求手写双向链表，见 [146](#/146)。

### `TreeMap` / `TreeSet` — 有序映射
<!-- match: \b(TreeMap|TreeSet)\b -->

红黑树，key 始终有序，增删查都是 O(log n)。需要「找比 x 大的最小值」这类操作时用。

```java
TreeMap<Integer, Integer> map = new TreeMap<>();
map.firstKey(); map.lastKey();
map.floorKey(x);     // <= x 的最大 key，没有返回 null
map.ceilingKey(x);   // >= x 的最小 key
map.lowerKey(x);     // <  x
map.higherKey(x);    // >  x
map.pollFirstEntry(); map.pollLastEntry();

TreeSet<Integer> set = new TreeSet<>();
set.first(); set.last(); set.floor(x); set.ceiling(x);
```

### `StringBuilder` — 可变字符串
<!-- match: \bStringBuilder\b -->

`String` 不可变，循环里用 `+` 拼接是 O(n²)，一律用 `StringBuilder`。

```java
StringBuilder sb = new StringBuilder();
sb.append(x);                    // 字符、数字、字符串都可以
sb.append(s, start, end);        // 追加 s[start, end)
sb.reverse();                    // 原地反转
sb.deleteCharAt(sb.length() - 1);    // 删掉最后一个字符（回溯撤销）
sb.insert(0, x);                 // 头插，O(n)
sb.charAt(i); sb.setCharAt(i, c);
sb.length();
sb.toString();
```

- `sb.append(a + b)` 里的 `+`：如果 `a`、`b` 都是 `char`，会先做整数加法。分开 `append`。
- 两个 `StringBuilder` 不能用 `equals` 比内容，先 `toString()`。

### `String` / `Character` 常用方法
<!-- match: \bCharacter\.\w+|\.toCharArray\(|\.split\(|\.compareTo\(|String\.join|String\.valueOf|\.trim\( -->

```java
s.length();  s.charAt(i);
s.substring(l, r);               // 左闭右开 [l, r)
s.toCharArray();                 // 转成 char[]，for (char c : s.toCharArray())
s.split("\\.");                  // 参数是正则：. | * + 等要转义；"\\s+" 是一个或多个空白
s.trim();                        // 去首尾空白，返回新串，要接住：s = s.trim()
s.equals(t);                     // 比较内容，不要用 ==
s.compareTo(t);                  // 字典序比较，负数表示 s 在前
s.indexOf("ab");  s.startsWith("ab");
String.valueOf(x);  Integer.parseInt(s);
String.join(".", list);          // 用分隔符拼接
new String(chars);  String.valueOf(chars);

Character.isDigit(c);  Character.isLetter(c);  Character.isLetterOrDigit(c);
Character.toLowerCase(c);
c - '0';                         // 数字字符 -> 数值
c - 'a';                         // 小写字母 -> 0~25
(char) ('a' + i);                // 反过来要强转
```

- `split` 的坑：开头有分隔符会多出一个空串（`" a b".split("\\s+")` 的第一个元素是 `""`），先 `trim()`。
- `char` 参与加法会变成 `int`：`'a' + 1` 是 98，不是 `'b'`。

### `Arrays` — 数组工具
<!-- match: \bArrays\. -->

```java
Arrays.sort(nums);                             // 升序
Arrays.sort(nums, l, r);                       // 只排 [l, r)
Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // 二维数组按第一列
Arrays.sort(strs, (a, b) -> (b + a).compareTo(a + b));   // 对象数组自定义比较
Arrays.fill(dp, -1);                           // 整个数组填同一个值（只能填一维）
Arrays.asList(1, 2, 3);                        // 固定长度的 List
Arrays.copyOfRange(nums, l, r);                // 拷贝 [l, r)
Arrays.toString(nums);                         // 打印调试
Arrays.equals(a, b);
```

- 基本类型数组（`int[]`）不能传比较器，想降序要么排完反转，要么用 `Integer[]`。
- 二维数组填充要逐行：`for (int[] row : memo) Arrays.fill(row, -1);`
- `Arrays.asList(arr)` 是数组的视图：不能增删，修改会反映到原数组（所以 `Collections.reverse(Arrays.asList(words))` 能把数组反过来）。

### `Collections` / `List` 常用操作
<!-- match: \bCollections\.|\bList\.of\b -->

```java
List<Integer> list = new ArrayList<>();
list.add(x);  list.get(i);  list.set(i, x);  list.size();
list.remove(list.size() - 1);          // 按下标删
list.remove(Integer.valueOf(x));       // 按值删（List<Integer> 传 int 会被当成下标）

List.of(a, b, c);                      // 不可变列表，直接当答案加入结果很方便
new ArrayList<>(path);                 // 拷贝

Collections.sort(list);
Collections.sort(list, (a, b) -> b - a);
Collections.reverse(list);
Collections.swap(list, i, j);
Collections.max(list);  Collections.min(list);

list.toArray(new int[0][]);            // List<int[]> -> int[][]
list.stream().mapToInt(Integer::intValue).toArray();   // List<Integer> -> int[]
```

- `List.of(...)` 返回的列表不能修改，也不能放 `null`。
- 返回空结果用 `new ArrayList<>()` 最稳。

### `Integer` / `Long` — 边界、溢出与类型转换
<!-- match: Integer\.(MAX_VALUE|MIN_VALUE|parseInt)|Long\.(MAX_VALUE|MIN_VALUE)|\(long\) -->

```java
Integer.MAX_VALUE   //  2147483647 ≈ 2.1e9
Integer.MIN_VALUE   // -2147483648
Long.MAX_VALUE      // ≈ 9.2e18

int mid = l + (r - l) / 2;        // 不写 (l + r) / 2，防溢出
long sq = (long) mid * mid;       // 先转 long 再乘；long sq = mid * mid 已经溢出了
Integer.parseInt("042");          // 42
Integer.compare(a, b);            // 比 a - b 安全的比较器写法
Math.abs(Integer.MIN_VALUE);      // 还是负数，溢出
```

- 用 `Integer.MAX_VALUE` 当「无穷大」时不能再 `+ 1`，会变成负数；DP 里常用 `amount + 1`、`n + 1` 这种「够大但加不爆」的值。
- 除法和取余都向零：`-7 / 2 == -3`，`-7 % 2 == -1`（Python 是 -4 和 1）。
- 整数除法想要小数结果：除以 `2.0`。

### `Random` — 随机数
<!-- match: \bRandom\b -->

```java
Random rand = new Random();
rand.nextInt(n);                  // [0, n)
lo + rand.nextInt(hi - lo + 1);   // [lo, hi]
```

- 快排 / 快速选择随机选 pivot：`nums[lo + rand.nextInt(hi - lo + 1)]`。
- `Random` 对象建一次放成员变量，不要在递归里反复 `new`。
