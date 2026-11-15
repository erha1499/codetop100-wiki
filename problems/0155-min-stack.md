---
rank: 64
id: "155"
title: 最小栈
difficulty: 简单
tags: [设计, 栈]
freq: 99
link: https://leetcode.cn/problems/min-stack/
desc: 设计一个栈，支持 push、pop、top，并能在 O(1) 时间取到当前最小值。
---
## 思路

- 空间换时间：除了正常的数据栈 `stk`，再维护一个**等长**的最小栈 `minStk`，`minStk[i]` = 数据栈前 `i + 1` 个元素里的最小值。
- `push`：新元素比 `minStk` 栈顶小就压新元素，否则把栈顶（当前最小值）再压一遍。
- `pop`：两个栈同步弹。`getMin` 就是 `minStk` 的栈顶。

## 易错点

- 最小值不变时也要重复压一遍：两个栈等长，弹栈时才能同步恢复出「弹之前的最小值」。
- 省空间的变体：只在 `val <= 最小值` 时才压 `minStk`，弹栈时要判断弹出的值是否等于 `minStk` 栈顶。Java 里这个比较是两个 `Integer`，要用 `equals`。

## 代码

```python
class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []                    # min_stk[i]：stk[0..i] 的最小值

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or val < self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
```

```java
class MinStack {
    private final Deque<Integer> stk = new ArrayDeque<>();
    private final Deque<Integer> minStk = new ArrayDeque<>();   // 与 stk 等长，栈顶是当前最小值

    public MinStack() {
    }

    public void push(int val) {
        stk.push(val);
        if (minStk.isEmpty() || val < minStk.peek()) {
            minStk.push(val);
        } else {
            minStk.push(minStk.peek());
        }
    }

    public void pop() {
        stk.pop();
        minStk.pop();
    }

    public int top() {
        return stk.peek();
    }

    public int getMin() {
        return minStk.peek();
    }
}
```

**复杂度**：各操作 O(1)，空间 O(n)。
