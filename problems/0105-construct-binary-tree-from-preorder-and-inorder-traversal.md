---
rank: 56
id: "105"
title: 从前序与中序遍历序列构造二叉树
difficulty: 中等
tags: [二叉树, 分治, 哈希表]
freq: 118
link: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
desc: 根据前序遍历和中序遍历的结果（无重复值）构造二叉树。
---
## 思路

- **前序定根，中序切左右**：前序区间的第一个元素 `pre[ps]` 是当前子树的根；在中序里找到根的位置 `index`，左边是左子树、右边是右子树。
- 左子树大小 `leftSize = index - is`，由此切出两个遍历里左右子树各自的区间：
  - 左子树：前序 `[ps + 1, ps + leftSize]`，中序 `[is, index - 1]`；
  - 右子树：前序 `[ps + leftSize + 1, pe]`，中序 `[index + 1, ie]`。
- 用哈希表预存「中序的值 → 下标」，找根 O(1)；全程传下标区间，不复制数组。

## 易错点

- `leftSize` 是 `index - is`，不是 `index`（只有 `is == 0` 时两者才相等）。
- 前序左子树从 `ps + 1` 开始。
- 每次线性找根或者 `copyOfRange` 切数组都会退化成 O(n²)。

## 代码

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {v: i for i, v in enumerate(inorder)}     # 中序：值 -> 下标

        def build(ps, pe, i_s, i_e):         # 前序 [ps, pe]，中序 [i_s, i_e]
            if ps > pe:
                return None
            root = TreeNode(preorder[ps])
            index = index_of[root.val]
            left_size = index - i_s
            root.left = build(ps + 1, ps + left_size, i_s, index - 1)
            root.right = build(ps + left_size + 1, pe, index + 1, i_e)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

```java
class Solution {
    private final Map<Integer, Integer> indexOf = new HashMap<>();   // 中序：值 -> 下标

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            indexOf.put(inorder[i], i);
        }
        return build(preorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }

    // 前序 [ps, pe]，中序 [is, ie]
    private TreeNode build(int[] pre, int ps, int pe, int is, int ie) {
        if (ps > pe) return null;
        TreeNode root = new TreeNode(pre[ps]);
        int index = indexOf.get(root.val);
        int leftSize = index - is;
        root.left = build(pre, ps + 1, ps + leftSize, is, index - 1);
        root.right = build(pre, ps + leftSize + 1, pe, index + 1, ie);
        return root;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
