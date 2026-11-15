---
rank: 4
id: "215"
title: 数组中的第K个最大元素
difficulty: 中等
tags: [排序, 快速选择, 堆]
freq: 608
link: https://leetcode.cn/problems/kth-largest-element-in-an-array/
desc: 求数组中第 k 大的元素（排序后的第 k 大，不去重）。
---
## 思路

- **快速选择**：第 k 大 = 升序后下标 `target = n - k`。每次 partition 后 pivot 落在最终位置，只需往 `target` 所在的那一侧继续找，平均 O(n)。
- **小顶堆**：堆里只留最大的 k 个，堆顶就是答案，O(n log k)；数据流或 k 很小时更合适。
- 手写堆（建堆 + siftDown）见 [补充题4](#/bu4) 的堆排序。

## 易错点

- pivot 要**随机选**，否则有序输入退化到 O(n²)。
- 用**三路划分**（`<`、`==`、`>`）：LeetCode 有大量重复元素的用例，双路划分会超时。原笔记里固定取 `nums[lo]` 的双路 partition 现在过不了。
- `target` 落在 `[lt, gt]` 内说明就是 pivot，直接返回。

## 代码

### 写法一：快速选择

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k               # 第 k 大 = 升序后的下标 n - k
        lo, hi = 0, len(nums) - 1
        while True:
            pivot = nums[random.randint(lo, hi)]
            lt, i, gt = lo, lo, hi           # [lo,lt) < pivot，[lt,i) == pivot，(gt,hi] > pivot
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            if target < lt:
                hi = lt - 1
            elif target > gt:
                lo = gt + 1
            else:
                return pivot
```

```java
class Solution {
    private final Random rand = new Random();

    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;            // 第 k 大 = 升序后的下标 n - k
        int lo = 0, hi = nums.length - 1;
        while (true) {
            int pivot = nums[lo + rand.nextInt(hi - lo + 1)];
            int lt = lo, i = lo, gt = hi;        // [lo,lt) < pivot，[lt,i) == pivot，(gt,hi] > pivot
            while (i <= gt) {
                if (nums[i] < pivot) swap(nums, lt++, i++);
                else if (nums[i] > pivot) swap(nums, i, gt--);
                else i++;
            }
            if (target < lt) hi = lt - 1;
            else if (target > gt) lo = gt + 1;
            else return pivot;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

### 写法二：大小为 k 的小顶堆

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []                            # 小顶堆，只留最大的 k 个
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();   // 小顶堆，只留最大的 k 个
        for (int x : nums) {
            pq.offer(x);
            if (pq.size() > k) pq.poll();
        }
        return pq.peek();
    }
}
```

**复杂度**：快速选择平均 O(n)、空间 O(1)；堆 O(n log k)、空间 O(k)。
