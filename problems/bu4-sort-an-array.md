---
rank: 9
id: "补充题4"
title: 手撕快速排序
difficulty: 中等
tags: [排序]
freq: 360
link: https://leetcode.cn/problems/sort-an-array/
desc: 手写排序（LeetCode 912 排序数组）：快排为主，归并、堆排也要会。
---
## 思路

- **快排** = 随机选 pivot + partition + 递归排左右两段。这里用三路划分：`< pivot | == pivot | > pivot`，中间一段已到位，只递归两边。
- **归并** = 排左半 + 排右半 + 合并两个有序数组（[88](#/88) / [21](#/21) 的思路）。稳定，固定 O(n log n)，要额外数组。
- **堆排** = 建大顶堆 → 堆顶换到末尾 → 堆范围减一 → 对堆顶 `siftDown`，重复。原地，不稳定。

## 易错点

- 快排必须随机化（随机 pivot 或先 shuffle），否则有序数组退化成 O(n²)。
- 912 有「全部相同」的大用例：`nums[i] <= pivot` 的双路 partition 每次只切下一个元素，会超时，所以用三路划分。
- 归并合并时 `tmp[i] <= tmp[j]` 取左边，保证稳定。
- 堆排：从最后一个非叶子节点 `n/2 - 1` 开始往前建堆；排序阶段 `siftDown(0, end)` 的堆大小是 `end` 不是 `n`，否则会破坏已排好的部分。

## 代码

### 快速排序

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(lo, hi):
            if lo >= hi:
                return
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
            quick_sort(lo, lt - 1)
            quick_sort(gt + 1, hi)

        quick_sort(0, len(nums) - 1)
        return nums
```

```java
class Solution {
    private final Random rand = new Random();

    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void quickSort(int[] nums, int lo, int hi) {
        if (lo >= hi) return;
        int pivot = nums[lo + rand.nextInt(hi - lo + 1)];
        int lt = lo, i = lo, gt = hi;            // [lo,lt) < pivot，[lt,i) == pivot，(gt,hi] > pivot
        while (i <= gt) {
            if (nums[i] < pivot) swap(nums, lt++, i++);
            else if (nums[i] > pivot) swap(nums, i, gt--);
            else i++;
        }
        quickSort(nums, lo, lt - 1);
        quickSort(nums, gt + 1, hi);
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

### 归并排序

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums)

        def merge_sort(lo, hi):
            if lo >= hi:
                return
            mid = (lo + hi) // 2
            merge_sort(lo, mid)
            merge_sort(mid + 1, hi)
            tmp[lo:hi + 1] = nums[lo:hi + 1]
            i, j = lo, mid + 1
            for k in range(lo, hi + 1):      # 合并 tmp[lo..mid] 和 tmp[mid+1..hi]
                if j > hi or (i <= mid and tmp[i] <= tmp[j]):
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1

        merge_sort(0, len(nums) - 1)
        return nums
```

```java
class Solution {
    private int[] tmp;

    public int[] sortArray(int[] nums) {
        tmp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void mergeSort(int[] nums, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        mergeSort(nums, lo, mid);
        mergeSort(nums, mid + 1, hi);
        for (int k = lo; k <= hi; k++) tmp[k] = nums[k];
        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++) {         // 合并 tmp[lo..mid] 和 tmp[mid+1..hi]
            if (j > hi || (i <= mid && tmp[i] <= tmp[j])) nums[k] = tmp[i++];
            else nums[k] = tmp[j++];
        }
    }
}
```

### 堆排序

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sift_down(i, n):                 # 在大小为 n 的大顶堆里把 i 下沉到位
            while True:
                l, r, mx = 2 * i + 1, 2 * i + 2, i
                if l < n and nums[l] > nums[mx]:
                    mx = l
                if r < n and nums[r] > nums[mx]:
                    mx = r
                if mx == i:
                    return
                nums[i], nums[mx] = nums[mx], nums[i]
                i = mx

        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):  # 建堆：从最后一个非叶子节点往前
            sift_down(i, n)
        for end in range(n - 1, 0, -1):      # 堆顶（最大）换到末尾，堆大小缩成 end
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)
        return nums
```

```java
class Solution {
    public int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = n / 2 - 1; i >= 0; i--) {   // 建堆：从最后一个非叶子节点往前
            siftDown(nums, i, n);
        }
        for (int end = n - 1; end > 0; end--) {  // 堆顶（最大）换到末尾，堆大小缩成 end
            swap(nums, 0, end);
            siftDown(nums, 0, end);
        }
        return nums;
    }

    // 在大小为 n 的大顶堆里把 i 下沉到位
    private void siftDown(int[] nums, int i, int n) {
        while (true) {
            int l = 2 * i + 1, r = 2 * i + 2, max = i;
            if (l < n && nums[l] > nums[max]) max = l;
            if (r < n && nums[r] > nums[max]) max = r;
            if (max == i) return;
            swap(nums, i, max);
            i = max;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

**复杂度**：快排平均 O(n log n)、最坏 O(n²)、空间 O(log n)；归并 O(n log n)、空间 O(n)；堆排 O(n log n)、空间 O(1)。
