# CodeTop 100 复习 wiki

[CodeTop](https://codetop.cc) 按考察频度排序的前 100 题（前 5 页）的复习笔记。面向**已经刷过、需要快速回忆**的场景：每题只保留思路、易错点和代码，Python / Java 双版本。

题目列表抓取于 2026-11-15，频度和排名以当时为准。

## 怎么用

- **网页**：直接用浏览器打开 `index.html`（单文件，数据内嵌，不需要服务器）。
- **GitHub 上直接看**：下面的[题目总表](#题目总表)点进每题的 Markdown；常用库速查见 [libs.md](libs.md)。

网页功能：

| 功能 | 说明 |
|---|---|
| 掌握程度 | 每题可标 生疏 / 模糊 / 熟练，侧栏顶部有总进度条，可按掌握程度筛选和排序 |
| 回忆模式 | 打开后只显示题目和一句话题意，自己先想，再按空格显示笔记 |
| 语言切换 | 代码块右上角切 Python / Java，全局生效并记住选择 |
| 筛选 / 搜索 | 按分类、掌握程度筛选；按题号、标题、分类搜索；可按频度 / 分类 / 掌握程度排序 |
| 跳转 | 每题有「去 LeetCode 做题」链接；笔记之间、笔记和常用库之间互相链接 |
| 常用库速查 | `heapq`、`deque`、`ArrayDeque`、`PriorityQueue` 等的用法和坑，并列出用到它的题 |

快捷键：`j` / `k`（或 `→` / `←`）切题，`1` `2` `3` 标记掌握程度（`0` 清除），`空格` 显示笔记，`l` 切语言，`r` 随机一题，`/` 搜索。

### 掌握程度存在哪

标记保存在浏览器的 localStorage 里（换浏览器 / 换设备不会同步）。仓库里的 `progress.json` 是初始值，页面上的标记会覆盖它。

想把进度存进仓库或者同步到另一台设备：页面左下角「导出进度」得到 `progress.json` → 覆盖仓库根目录的同名文件 → `python3 scripts/build.py` → 提交。另一台设备上也可以直接「导入进度」。

## 目录

```
index.html            生成的页面（不要手改）
problems/*.md         每题一个文件：front matter + 思路 / 易错点 / 代码
libs.md               算法常用库速查（Python / Java）
progress.json         掌握程度的初始值
scripts/build.py      problems/*.md + libs.md -> index.html，并刷新本文件的题目总表
scripts/check.py      跑一遍所有笔记里的 Python / Java 代码
scripts/cases.py      check.py 用的测试用例
scripts/template.html 页面模板（样式和交互都在这里）
```

## 改笔记

直接编辑 `problems/` 下的 Markdown，然后：

```bash
python3 scripts/build.py     # 重新生成 index.html
python3 scripts/check.py     # 可选：校验所有代码（Java 部分需要 JDK；--no-java 只跑 Python）
```

约定：

- 文件开头的 front matter 是题目信息（`rank` 频度排名、`id` 题号、`tags` 分类、`desc` 一句话题意…），`tags` 的第一个是主分类。
- 正文支持的 Markdown：标题、列表、代码块、行内代码、加粗、链接、引用。
- 紧挨着的 ` ```python ` 和 ` ```java ` 代码块会在页面上合成一组，可以切换。
- 笔记之间互相引用写 `[146](#/146)`；括号里是文件名的前缀去掉前导 0。
- 代码按 LeetCode 提交格式写，省略了 import（见 [libs.md](libs.md) 开头的说明）。
- `libs.md` 里每个 `###` 小节下面的 `<!-- match: 正则 -->` 决定哪些题目会被关联到这一节。

## 题目总表

<!-- LIST:START -->
| # | 题目 | 难度 | 分类 | 原题 |
|--:|---|---|---|---|
| 1 | [3. 无重复字符的最长子串](problems/0003-longest-substring-without-repeating-characters.md) | 中等 | 滑动窗口 · 哈希表 | [LeetCode](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) |
| 2 | [146. LRU缓存机制](problems/0146-lru-cache.md) | 中等 | 设计 · 哈希表 · 链表 | [LeetCode](https://leetcode.cn/problems/lru-cache/) |
| 3 | [206. 反转链表](problems/0206-reverse-linked-list.md) | 简单 | 链表 | [LeetCode](https://leetcode.cn/problems/reverse-linked-list/) |
| 4 | [215. 数组中的第K个最大元素](problems/0215-kth-largest-element-in-an-array.md) | 中等 | 排序 · 快速选择 · 堆 | [LeetCode](https://leetcode.cn/problems/kth-largest-element-in-an-array/) |
| 5 | [25. K 个一组翻转链表](problems/0025-reverse-nodes-in-k-group.md) | 困难 | 链表 | [LeetCode](https://leetcode.cn/problems/reverse-nodes-in-k-group/) |
| 6 | [15. 三数之和](problems/0015-3sum.md) | 中等 | 双指针 · 排序 | [LeetCode](https://leetcode.cn/problems/3sum/) |
| 7 | [53. 最大子数组和](problems/0053-maximum-subarray.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/maximum-subarray/) |
| 8 | [5. 最长回文子串](problems/0005-longest-palindromic-substring.md) | 中等 | 字符串 · 双指针 | [LeetCode](https://leetcode.cn/problems/longest-palindromic-substring/) |
| 9 | [补充题4. 手撕快速排序](problems/bu4-sort-an-array.md) | 中等 | 排序 | [LeetCode](https://leetcode.cn/problems/sort-an-array/) |
| 10 | [200. 岛屿数量](problems/0200-number-of-islands.md) | 中等 | 图 · DFS · BFS · 矩阵 | [LeetCode](https://leetcode.cn/problems/number-of-islands/) |
| 11 | [21. 合并两个有序链表](problems/0021-merge-two-sorted-lists.md) | 简单 | 链表 | [LeetCode](https://leetcode.cn/problems/merge-two-sorted-lists/) |
| 12 | [102. 二叉树的层序遍历](problems/0102-binary-tree-level-order-traversal.md) | 中等 | 二叉树 · BFS | [LeetCode](https://leetcode.cn/problems/binary-tree-level-order-traversal/) |
| 13 | [33. 搜索旋转排序数组](problems/0033-search-in-rotated-sorted-array.md) | 中等 | 二分 | [LeetCode](https://leetcode.cn/problems/search-in-rotated-sorted-array/) |
| 14 | [46. 全排列](problems/0046-permutations.md) | 中等 | 回溯 | [LeetCode](https://leetcode.cn/problems/permutations/) |
| 15 | [1. 两数之和](problems/0001-two-sum.md) | 简单 | 哈希表 | [LeetCode](https://leetcode.cn/problems/two-sum/) |
| 16 | [88. 合并两个有序数组](problems/0088-merge-sorted-array.md) | 简单 | 双指针 · 数组 | [LeetCode](https://leetcode.cn/problems/merge-sorted-array/) |
| 17 | [20. 有效的括号](problems/0020-valid-parentheses.md) | 简单 | 栈 · 字符串 | [LeetCode](https://leetcode.cn/problems/valid-parentheses/) |
| 18 | [121. 买卖股票的最佳时机](problems/0121-best-time-to-buy-and-sell-stock.md) | 简单 | 贪心 · 动态规划 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) |
| 19 | [300. 最长上升子序列](problems/0300-longest-increasing-subsequence.md) | 中等 | 动态规划 · 二分 | [LeetCode](https://leetcode.cn/problems/longest-increasing-subsequence/) |
| 20 | [236. 二叉树的最近公共祖先](problems/0236-lowest-common-ancestor-of-a-binary-tree.md) | 中等 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 21 | [103. 二叉树的锯齿形层次遍历](problems/0103-binary-tree-zigzag-level-order-traversal.md) | 中等 | 二叉树 · BFS | [LeetCode](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) |
| 22 | [92. 反转链表 II](problems/0092-reverse-linked-list-ii.md) | 中等 | 链表 | [LeetCode](https://leetcode.cn/problems/reverse-linked-list-ii/) |
| 23 | [23. 合并K个排序链表](problems/0023-merge-k-sorted-lists.md) | 困难 | 链表 · 分治 · 堆 | [LeetCode](https://leetcode.cn/problems/merge-k-sorted-lists/) |
| 24 | [54. 螺旋矩阵](problems/0054-spiral-matrix.md) | 中等 | 矩阵 · 模拟 | [LeetCode](https://leetcode.cn/problems/spiral-matrix/) |
| 25 | [143. 重排链表](problems/0143-reorder-list.md) | 中等 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/reorder-list/) |
| 26 | [141. 环形链表](problems/0141-linked-list-cycle.md) | 简单 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/linked-list-cycle/) |
| 27 | [56. 合并区间](problems/0056-merge-intervals.md) | 中等 | 排序 · 数组 | [LeetCode](https://leetcode.cn/problems/merge-intervals/) |
| 28 | [415. 字符串相加](problems/0415-add-strings.md) | 简单 | 字符串 · 模拟 | [LeetCode](https://leetcode.cn/problems/add-strings/) |
| 29 | [72. 编辑距离](problems/0072-edit-distance.md) | 困难 | 动态规划 · 字符串 | [LeetCode](https://leetcode.cn/problems/edit-distance/) |
| 30 | [1143. 最长公共子序列](problems/1143-longest-common-subsequence.md) | 中等 | 动态规划 · 字符串 | [LeetCode](https://leetcode.cn/problems/longest-common-subsequence/) |
| 31 | [160. 相交链表](problems/0160-intersection-of-two-linked-lists.md) | 简单 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/intersection-of-two-linked-lists/) |
| 32 | [42. 接雨水](problems/0042-trapping-rain-water.md) | 困难 | 双指针 · 数组 | [LeetCode](https://leetcode.cn/problems/trapping-rain-water/) |
| 33 | [19. 删除链表的倒数第N个节点](problems/0019-remove-nth-node-from-end-of-list.md) | 中等 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) |
| 34 | [93. 复原IP地址](problems/0093-restore-ip-addresses.md) | 中等 | 回溯 · 字符串 | [LeetCode](https://leetcode.cn/problems/restore-ip-addresses/) |
| 35 | [124. 二叉树中的最大路径和](problems/0124-binary-tree-maximum-path-sum.md) | 困难 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) |
| 36 | [82. 删除排序链表中的重复元素 II](problems/0082-remove-duplicates-from-sorted-list-ii.md) | 中等 | 链表 | [LeetCode](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/) |
| 37 | [4. 寻找两个正序数组的中位数](problems/0004-median-of-two-sorted-arrays.md) | 困难 | 二分 · 数组 | [LeetCode](https://leetcode.cn/problems/median-of-two-sorted-arrays/) |
| 38 | [142. 环形链表 II](problems/0142-linked-list-cycle-ii.md) | 中等 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/linked-list-cycle-ii/) |
| 39 | [165. 比较版本号](problems/0165-compare-version-numbers.md) | 中等 | 字符串 · 双指针 | [LeetCode](https://leetcode.cn/problems/compare-version-numbers/) |
| 40 | [199. 二叉树的右视图](problems/0199-binary-tree-right-side-view.md) | 中等 | 二叉树 · BFS · DFS | [LeetCode](https://leetcode.cn/problems/binary-tree-right-side-view/) |
| 41 | [239. 滑动窗口最大值](problems/0239-sliding-window-maximum.md) | 困难 | 滑动窗口 · 单调队列 | [LeetCode](https://leetcode.cn/problems/sliding-window-maximum/) |
| 42 | [704. 二分查找](problems/0704-binary-search.md) | 简单 | 二分 | [LeetCode](https://leetcode.cn/problems/binary-search/) |
| 43 | [22. 括号生成](problems/0022-generate-parentheses.md) | 中等 | 回溯 · 字符串 | [LeetCode](https://leetcode.cn/problems/generate-parentheses/) |
| 44 | [32. 最长有效括号](problems/0032-longest-valid-parentheses.md) | 困难 | 栈 · 动态规划 · 字符串 | [LeetCode](https://leetcode.cn/problems/longest-valid-parentheses/) |
| 45 | [69. x 的平方根](problems/0069-sqrtx.md) | 简单 | 二分 · 数学 | [LeetCode](https://leetcode.cn/problems/sqrtx/) |
| 46 | [148. 排序链表](problems/0148-sort-list.md) | 中等 | 链表 · 排序 · 分治 | [LeetCode](https://leetcode.cn/problems/sort-list/) |
| 47 | [94. 二叉树的中序遍历](problems/0094-binary-tree-inorder-traversal.md) | 简单 | 二叉树 · 栈 | [LeetCode](https://leetcode.cn/problems/binary-tree-inorder-traversal/) |
| 48 | [232. 用栈实现队列](problems/0232-implement-queue-using-stacks.md) | 简单 | 设计 · 栈 | [LeetCode](https://leetcode.cn/problems/implement-queue-using-stacks/) |
| 49 | [31. 下一个排列](problems/0031-next-permutation.md) | 中等 | 数组 · 双指针 | [LeetCode](https://leetcode.cn/problems/next-permutation/) |
| 50 | [322. 零钱兑换](problems/0322-coin-change.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/coin-change/) |
| 51 | [76. 最小覆盖子串](problems/0076-minimum-window-substring.md) | 困难 | 滑动窗口 · 哈希表 | [LeetCode](https://leetcode.cn/problems/minimum-window-substring/) |
| 52 | [70. 爬楼梯](problems/0070-climbing-stairs.md) | 简单 | 动态规划 | [LeetCode](https://leetcode.cn/problems/climbing-stairs/) |
| 53 | [43. 字符串相乘](problems/0043-multiply-strings.md) | 中等 | 字符串 · 模拟 | [LeetCode](https://leetcode.cn/problems/multiply-strings/) |
| 54 | [8. 字符串转换整数 (atoi)](problems/0008-string-to-integer-atoi.md) | 中等 | 字符串 · 模拟 | [LeetCode](https://leetcode.cn/problems/string-to-integer-atoi/) |
| 55 | [2. 两数相加](problems/0002-add-two-numbers.md) | 中等 | 链表 · 模拟 | [LeetCode](https://leetcode.cn/problems/add-two-numbers/) |
| 56 | [105. 从前序与中序遍历序列构造二叉树](problems/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) | 中等 | 二叉树 · 分治 · 哈希表 | [LeetCode](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 57 | [41. 缺失的第一个正数](problems/0041-first-missing-positive.md) | 困难 | 数组 · 哈希表 | [LeetCode](https://leetcode.cn/problems/first-missing-positive/) |
| 58 | [78. 子集](problems/0078-subsets.md) | 中等 | 回溯 | [LeetCode](https://leetcode.cn/problems/subsets/) |
| 59 | [151. 翻转字符串里的单词](problems/0151-reverse-words-in-a-string.md) | 中等 | 字符串 · 双指针 | [LeetCode](https://leetcode.cn/problems/reverse-words-in-a-string/) |
| 60 | [34. 在排序数组中查找元素的第一个和最后一个位置](problems/0034-find-first-and-last-position-of-element-in-sorted-array.md) | 中等 | 二分 | [LeetCode](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 61 | [394. 字符串解码](problems/0394-decode-string.md) | 中等 | 栈 · 字符串 | [LeetCode](https://leetcode.cn/problems/decode-string/) |
| 62 | [剑指 Offer 22. 链表中倒数第k个节点](problems/offer22-kth-node-from-end.md) | 简单 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/) |
| 63 | [129. 求根到叶子节点数字之和](problems/0129-sum-root-to-leaf-numbers.md) | 中等 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) |
| 64 | [155. 最小栈](problems/0155-min-stack.md) | 简单 | 设计 · 栈 | [LeetCode](https://leetcode.cn/problems/min-stack/) |
| 65 | [695. 岛屿的最大面积](problems/0695-max-area-of-island.md) | 中等 | 图 · DFS · BFS · 矩阵 | [LeetCode](https://leetcode.cn/problems/max-area-of-island/) |
| 66 | [128. 最长连续序列](problems/0128-longest-consecutive-sequence.md) | 中等 | 哈希表 · 数组 | [LeetCode](https://leetcode.cn/problems/longest-consecutive-sequence/) |
| 67 | [470. 用 Rand7() 实现 Rand10()](problems/0470-implement-rand10-using-rand7.md) | 中等 | 数学 · 概率 | [LeetCode](https://leetcode.cn/problems/implement-rand10-using-rand7/) |
| 68 | [64. 最小路径和](problems/0064-minimum-path-sum.md) | 中等 | 动态规划 · 矩阵 | [LeetCode](https://leetcode.cn/problems/minimum-path-sum/) |
| 69 | [101. 对称二叉树](problems/0101-symmetric-tree.md) | 简单 | 二叉树 · DFS · BFS | [LeetCode](https://leetcode.cn/problems/symmetric-tree/) |
| 70 | [39. 组合总和](problems/0039-combination-sum.md) | 中等 | 回溯 | [LeetCode](https://leetcode.cn/problems/combination-sum/) |
| 71 | [104. 二叉树的最大深度](problems/0104-maximum-depth-of-binary-tree.md) | 简单 | 二叉树 · DFS · BFS | [LeetCode](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) |
| 72 | [152. 乘积最大子数组](problems/0152-maximum-product-subarray.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/maximum-product-subarray/) |
| 73 | [122. 买卖股票的最佳时机 II](problems/0122-best-time-to-buy-and-sell-stock-ii.md) | 简单 | 贪心 | [LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) |
| 74 | [110. 平衡二叉树](problems/0110-balanced-binary-tree.md) | 简单 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/balanced-binary-tree/) |
| 75 | [221. 最大正方形](problems/0221-maximal-square.md) | 中等 | 动态规划 · 矩阵 | [LeetCode](https://leetcode.cn/problems/maximal-square/) |
| 76 | [234. 回文链表](problems/0234-palindrome-linked-list.md) | 简单 | 链表 · 双指针 | [LeetCode](https://leetcode.cn/problems/palindrome-linked-list/) |
| 77 | [179. 最大数](problems/0179-largest-number.md) | 中等 | 排序 · 字符串 · 贪心 | [LeetCode](https://leetcode.cn/problems/largest-number/) |
| 78 | [14. 最长公共前缀](problems/0014-longest-common-prefix.md) | 简单 | 字符串 | [LeetCode](https://leetcode.cn/problems/longest-common-prefix/) |
| 79 | [48. 旋转图像](problems/0048-rotate-image.md) | 中等 | 矩阵 | [LeetCode](https://leetcode.cn/problems/rotate-image/) |
| 80 | [240. 搜索二维矩阵 II](problems/0240-search-a-2d-matrix-ii.md) | 中等 | 矩阵 · 双指针 | [LeetCode](https://leetcode.cn/problems/search-a-2d-matrix-ii/) |
| 81 | [560. 和为K的子数组](problems/0560-subarray-sum-equals-k.md) | 中等 | 哈希表 · 前缀和 | [LeetCode](https://leetcode.cn/problems/subarray-sum-equals-k/) |
| 82 | [662. 二叉树最大宽度](problems/0662-maximum-width-of-binary-tree.md) | 中等 | 二叉树 · BFS · DFS | [LeetCode](https://leetcode.cn/problems/maximum-width-of-binary-tree/) |
| 83 | [98. 验证二叉搜索树](problems/0098-validate-binary-search-tree.md) | 中等 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/validate-binary-search-tree/) |
| 84 | [144. 二叉树的前序遍历](problems/0144-binary-tree-preorder-traversal.md) | 简单 | 二叉树 · 栈 | [LeetCode](https://leetcode.cn/problems/binary-tree-preorder-traversal/) |
| 85 | [543. 二叉树的直径](problems/0543-diameter-of-binary-tree.md) | 简单 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/diameter-of-binary-tree/) |
| 86 | [162. 寻找峰值](problems/0162-find-peak-element.md) | 中等 | 二分 | [LeetCode](https://leetcode.cn/problems/find-peak-element/) |
| 87 | [113. 路径总和 II](problems/0113-path-sum-ii.md) | 中等 | 二叉树 · 回溯 | [LeetCode](https://leetcode.cn/problems/path-sum-ii/) |
| 88 | [62. 不同路径](problems/0062-unique-paths.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/unique-paths/) |
| 89 | [198. 打家劫舍](problems/0198-house-robber.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/house-robber/) |
| 90 | [209. 长度最小的子数组](problems/0209-minimum-size-subarray-sum.md) | 中等 | 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-size-subarray-sum/) |
| 91 | [24. 两两交换链表中的节点](problems/0024-swap-nodes-in-pairs.md) | 中等 | 链表 | [LeetCode](https://leetcode.cn/problems/swap-nodes-in-pairs/) |
| 92 | [139. 单词拆分](problems/0139-word-break.md) | 中等 | 动态规划 · 字符串 · 哈希表 | [LeetCode](https://leetcode.cn/problems/word-break/) |
| 93 | [112. 路径总和](problems/0112-path-sum.md) | 简单 | 二叉树 · DFS | [LeetCode](https://leetcode.cn/problems/path-sum/) |
| 94 | [718. 最长重复子数组](problems/0718-maximum-length-of-repeated-subarray.md) | 中等 | 动态规划 | [LeetCode](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) |
| 95 | [227. 基本计算器 II](problems/0227-basic-calculator-ii.md) | 中等 | 栈 · 字符串 | [LeetCode](https://leetcode.cn/problems/basic-calculator-ii/) |
| 96 | [207. 课程表](problems/0207-course-schedule.md) | 中等 | 图 · DFS · BFS | [LeetCode](https://leetcode.cn/problems/course-schedule/) |
| 97 | [83. 删除排序链表中的重复元素](problems/0083-remove-duplicates-from-sorted-list.md) | 简单 | 链表 | [LeetCode](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) |
| 98 | [283. 移动零](problems/0283-move-zeroes.md) | 简单 | 双指针 · 数组 | [LeetCode](https://leetcode.cn/problems/move-zeroes/) |
| 99 | [226. 翻转二叉树](problems/0226-invert-binary-tree.md) | 简单 | 二叉树 · DFS · BFS | [LeetCode](https://leetcode.cn/problems/invert-binary-tree/) |
| 100 | [169. 多数元素](problems/0169-majority-element.md) | 简单 | 数组 | [LeetCode](https://leetcode.cn/problems/majority-element/) |
<!-- LIST:END -->
