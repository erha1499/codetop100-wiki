---
rank: 48
id: "232"
title: 用栈实现队列
difficulty: 简单
tags: [设计, 栈]
freq: 143
link: https://leetcode.cn/problems/implement-queue-using-stacks/
desc: 只用两个栈实现先进先出的队列（push、pop、peek、empty）。
---
## 思路

- 双栈：`stk1` 是输入栈，负责 `push`；`stk2` 是输出栈，负责 `pop` / `peek`。
- 出队或看队首时，**只有 `stk2` 为空**才把 `stk1` 的元素全部倒进 `stk2`——倒一次顺序就反过来了，栈顶正好是最早进来的。
- 懒搬运：每个元素最多进 `stk1` 一次、搬一次、出 `stk2` 一次，均摊 O(1)。

## 易错点

- `stk2` 不为空时不能搬，否则顺序就乱了。把这段逻辑抽成 `refresh()`，`pop` 和 `peek` 之前都调用。
- 两个栈都空才算队列为空。

## 代码

```python
class MyQueue:
    def __init__(self):
        self.stk1 = []                       # 输入栈
        self.stk2 = []                       # 输出栈

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.refresh()
        return self.stk2.pop()

    def peek(self) -> int:
        self.refresh()
        return self.stk2[-1]

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2

    def refresh(self):
        if not self.stk2:                    # 输出栈空了才搬
            while self.stk1:
                self.stk2.append(self.stk1.pop())
```

```java
class MyQueue {
    private final Deque<Integer> stk1 = new ArrayDeque<>();   // 输入栈
    private final Deque<Integer> stk2 = new ArrayDeque<>();   // 输出栈

    public MyQueue() {
    }

    public void push(int x) {
        stk1.push(x);
    }

    public int pop() {
        refresh();
        return stk2.pop();
    }

    public int peek() {
        refresh();
        return stk2.peek();
    }

    public boolean empty() {
        return stk1.isEmpty() && stk2.isEmpty();
    }

    private void refresh() {
        if (stk2.isEmpty()) {                // 输出栈空了才搬
            while (!stk1.isEmpty()) {
                stk2.push(stk1.pop());
            }
        }
    }
}
```

**复杂度**：各操作均摊 O(1)，空间 O(n)。
