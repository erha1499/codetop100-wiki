#!/usr/bin/env python3
"""校验 problems/*.md 里的 Python / Java 代码能跑、结果对。

    python3 scripts/check.py            # 全部
    python3 scripts/check.py 3 146 bu4  # 只跑指定题（用文件名前缀，去掉前导 0）
    python3 scripts/check.py --no-java  # 没装 JDK 时只跑 Python

用例在 scripts/cases.py。同一份用例同时驱动两种语言：
参数/返回值的类型从 Java 方法签名里解析（ListNode、TreeNode 会自动互转）。
"""
import copy
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, code_blocks, parse_front_matter  # noqa: E402
from cases import CASES  # noqa: E402

# ---------------------------------------------------------------- Python 侧

PRELUDE = """
from typing import *
from collections import *
from functools import *
from itertools import *
from heapq import *
from bisect import *
from math import inf
import heapq, bisect, random, math, collections, functools

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

_rng = random.Random(7)
def rand7():
    return _rng.randint(1, 7)
"""


class Helper:
    """给自定义用例用的工具，Java 侧有同名的 lc.H。"""

    def __init__(self, ns):
        self.ns = ns

    def list(self, *vals):
        dummy = tail = self.ns["ListNode"]()
        for v in vals:
            tail.next = self.ns["ListNode"](v)
            tail = tail.next
        return dummy.next

    def cycle(self, pos, *vals):
        head = self.list(*vals)
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return head

    def node(self, head, idx):
        for _ in range(idx):
            head = head.next
        return head

    def join(self, a, b):
        """把链表 b 接到 a 的尾部（共享 b 的节点），返回头。"""
        if not a:
            return b
        tail = a
        while tail.next:
            tail = tail.next
        tail.next = b
        return a

    def tree(self, *vals):
        if not vals or vals[0] is None:
            return None
        T = self.ns["TreeNode"]
        root = T(vals[0])
        queue, i = [root], 1
        while i < len(vals):
            node = queue.pop(0)
            if vals[i] is not None:
                node.left = T(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = T(vals[i])
                queue.append(node.right)
            i += 1
        return root

    def find(self, root, val):
        if not root or root.val == val:
            return root
        return self.find(root.left, val) or self.find(root.right, val)


def to_plain(v):
    """ListNode / TreeNode / 元组 → 纯 JSON 结构。"""
    name = type(v).__name__
    if name == "ListNode":
        out = []
        while v and len(out) < 10000:
            out.append(v.val)
            v = v.next
        return out
    if name == "TreeNode":
        out, queue = [], [v]
        while queue:
            node = queue.pop(0)
            out.append(node.val if node else None)
            if node:
                queue += [node.left, node.right]
        while out and out[-1] is None:
            out.pop()
        return out
    if isinstance(v, (list, tuple)):
        return [to_plain(x) for x in v]
    return v


def py_arg(helper, jtype, value):
    if jtype == "ListNode":
        return helper.list(*value)
    if jtype == "ListNode[]":
        return [helper.list(*v) for v in value]
    if jtype == "TreeNode":
        return helper.tree(*value)
    return copy.deepcopy(value)


def same(a, b):
    if a is None and b == [] or a == [] and b is None:      # 空链表 / 空树
        return True
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def normalize(v, mode):
    if mode and isinstance(v, list):
        if mode == "deep":
            v = [sorted(x, key=json.dumps) if isinstance(x, list) else x for x in v]
        v = sorted(v, key=json.dumps)
    return v


# ---------------------------------------------------------------- Java 侧

JAVA_LC = {
    "ListNode.java": """package lc;
public class ListNode {
    public int val; public ListNode next;
    public ListNode() {}
    public ListNode(int val) { this.val = val; }
    public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}""",
    "TreeNode.java": """package lc;
public class TreeNode {
    public int val; public TreeNode left, right;
    public TreeNode() {}
    public TreeNode(int val) { this.val = val; }
    public TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }
}""",
    "SolBase.java": """package lc;
public class SolBase {
    private static final java.util.Random R = new java.util.Random(7);
    public int rand7() { return R.nextInt(7) + 1; }
}""",
    "H.java": r"""package lc;
import java.util.*;
public class H {
    public interface Case { Object get() throws Exception; }
    public static void run(String id, int idx, Case c) {
        String s;
        try { s = str(c.get()); } catch (Throwable e) { s = str("!ERR " + e); }
        System.out.println("R\t" + id + "\t" + idx + "\t" + s);
    }
    public static ListNode list(int... a) {
        ListNode d = new ListNode(), t = d;
        for (int x : a) { t.next = new ListNode(x); t = t.next; }
        return d.next;
    }
    public static ListNode cycle(int pos, int... a) {
        ListNode h = list(a);
        if (pos >= 0) { ListNode t = h; while (t.next != null) t = t.next; t.next = node(h, pos); }
        return h;
    }
    public static ListNode node(ListNode h, int idx) { while (idx-- > 0) h = h.next; return h; }
    public static ListNode join(ListNode a, ListNode b) {
        if (a == null) return b;
        ListNode t = a;
        while (t.next != null) t = t.next;
        t.next = b;
        return a;
    }
    public static TreeNode tree(Integer... a) {
        if (a.length == 0 || a[0] == null) return null;
        TreeNode root = new TreeNode(a[0]);
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (i < a.length) {
            TreeNode n = q.poll();
            if (a[i] != null) { n.left = new TreeNode(a[i]); q.add(n.left); }
            i++;
            if (i < a.length && a[i] != null) { n.right = new TreeNode(a[i]); q.add(n.right); }
            i++;
        }
        return root;
    }
    public static TreeNode find(TreeNode r, int v) {
        if (r == null || r.val == v) return r;
        TreeNode l = find(r.left, v);
        return l != null ? l : find(r.right, v);
    }
    public static String str(Object o) {
        if (o == null) return "null";
        if (o instanceof String || o instanceof Character) {
            StringBuilder sb = new StringBuilder("\"");
            for (char c : o.toString().toCharArray()) {
                if (c == '"' || c == '\\') sb.append('\\').append(c);
                else if (c < 32) sb.append(String.format("\\u%04x", (int) c));
                else sb.append(c);
            }
            return sb.append('"').toString();
        }
        if (o instanceof Number || o instanceof Boolean) return o.toString();
        List<String> parts = new ArrayList<>();
        if (o instanceof int[]) for (int x : (int[]) o) parts.add(String.valueOf(x));
        else if (o instanceof char[]) for (char x : (char[]) o) parts.add(str(x));
        else if (o instanceof Object[]) for (Object x : (Object[]) o) parts.add(str(x));
        else if (o instanceof Collection) for (Object x : (Collection<?>) o) parts.add(str(x));
        else if (o instanceof ListNode) {
            for (ListNode p = (ListNode) o; p != null && parts.size() < 10000; p = p.next) parts.add(String.valueOf(p.val));
        } else if (o instanceof TreeNode) {
            List<TreeNode> q = new ArrayList<>();
            q.add((TreeNode) o);
            for (int i = 0; i < q.size(); i++) {
                TreeNode n = q.get(i);
                parts.add(n == null ? "null" : String.valueOf(n.val));
                if (n != null) { q.add(n.left); q.add(n.right); }
            }
            while (!parts.isEmpty() && parts.get(parts.size() - 1).equals("null")) parts.remove(parts.size() - 1);
        } else return str(o.toString());
        return "[" + String.join(",", parts) + "]";
    }
}""",
}


def split_params(text):
    parts, depth, cur = [], 0, ""
    for ch in text:
        depth += (ch == "<") - (ch == ">")
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return [p.strip().rsplit(None, 1)[0].replace(" ", "") for p in parts]


def java_signature(src, name):
    """返回 (返回类型, [参数类型])；找不到返回 None。"""
    m = re.search(rf"(?:public\s+)?([\w<>\[\], ]+?)\s+{re.escape(name)}\s*\(([^)]*)\)\s*\{{", src)
    if not m:
        return None
    ret = re.sub(r"\b(public|private|protected|static|final)\b", "", m[1]).replace(" ", "")
    if ret in ("", "new", "return", "else"):
        return None
    return ret, split_params(m[2])


def jlit(jtype, v, top=True):
    if jtype.endswith("[]"):
        body = "{" + ",".join(jlit(jtype[:-2], x, False) for x in v) + "}"
        return f"new {jtype}{body}" if top else body
    if m := re.match(r"List<(.+)>$", jtype):
        return "new ArrayList<>(Arrays.asList(" + ",".join(jlit(m[1], x) for x in v) + "))"
    if jtype == "ListNode":
        return f"H.list({','.join(map(str, v))})"
    if jtype == "TreeNode":
        return "H.tree(" + ",".join("null" if x is None else str(x) for x in v) + ")"
    if jtype in ("String",):
        return json.dumps(v, ensure_ascii=False)
    if jtype in ("char", "Character"):
        return "'" + v + "'"
    if jtype in ("boolean", "Boolean"):
        return "true" if v else "false"
    if jtype == "long":
        return f"{v}L"
    return str(v)


def java_main(pkg, src, spec):
    """生成一个包里的 Main.run()；返回 None 表示这段代码不含被测目标。"""
    cases = []
    if spec["kind"] == "fn":
        sig = java_signature(src, spec["name"])
        if not sig or "class Solution" not in src:
            return None
        ret, params = sig
        for args, _ in spec["cases"]:
            decl = "".join(f"{t} a{i} = {jlit(t, a)}; " for i, (t, a) in enumerate(zip(params, args)))
            call = f"new Solution().{spec['name']}({','.join(f'a{i}' for i in range(len(params)))})"
            cases.append(f"{decl}{call}; return a0;" if ret == "void" else f"{decl}return {call};")
    elif spec["kind"] == "design":
        if f"class {spec['cls']}" not in src:
            return None
        ops, args = spec["ops"], spec["args"]
        body = [f"{spec['cls']} obj = new {spec['cls']}({','.join(map(str, args[0]))});",
                "List<Object> out = new ArrayList<>(); out.add(null);"]
        for op, arg in zip(ops[1:], args[1:]):
            sig = java_signature(src, op)
            call = f"obj.{op}({','.join(map(str, arg))})"
            body.append(f"{call}; out.add(null);" if sig and sig[0] == "void" else f"out.add({call});")
        cases.append(" ".join(body) + " return out;")
    else:  # custom
        if spec["need"] not in src:
            return None
        cases = [c[1] for c in spec["cases"]]
    runs = "\n".join(f'        H.run("{pkg}", {i}, () -> {{ {c} }});' for i, c in enumerate(cases))
    return (f"package {pkg};\nimport java.util.*;\nimport lc.*;\n"
            f"public class Main {{\n    public static void run() {{\n{runs}\n    }}\n}}\n")


# ---------------------------------------------------------------- 主流程

def expected_of(spec):
    if spec["kind"] == "design":
        return [spec["expected"]]
    return [c[-1] for c in spec["cases"]]


def run_python(src, spec, sig_types):
    """返回每个用例的结果列表；这段代码不含被测目标时返回 None。"""
    ns = {}
    exec(PRELUDE + "\n" + src, ns)  # noqa: S102 - 只执行仓库里自己的笔记代码
    helper = Helper(ns)
    if spec["kind"] == "fn":
        if "Solution" not in ns or not hasattr(ns["Solution"], spec["name"]):
            return None
        ret, params = sig_types or ("?", [])
        out = []
        for args, _ in spec["cases"]:
            types = params if len(params) == len(args) else ["?"] * len(args)
            conv = [py_arg(helper, t, a) for t, a in zip(types, args)]
            res = getattr(ns["Solution"](), spec["name"])(*conv)
            out.append(to_plain(conv[0] if ret == "void" else res))
        return out
    if spec["kind"] == "design":
        if spec["cls"] not in ns:
            return None
        obj = ns[spec["cls"]](*spec["args"][0])
        return [[None] + [getattr(obj, op)(*arg) for op, arg in zip(spec["ops"][1:], spec["args"][1:])]]
    if spec["need"] not in src:
        return None
    return [to_plain(c[0](ns, helper)) for c in spec["cases"]]


def compare(label, got, spec, failures):
    want = expected_of(spec)
    mode = spec.get("unordered")
    for i, (g, w) in enumerate(zip(got, want)):
        if not same(normalize(g, mode), normalize(w, mode)):
            failures.append(f"{label} 用例 {i}: 期望 {json.dumps(w, ensure_ascii=False)}，得到 {json.dumps(g, ensure_ascii=False)}")
    if len(got) != len(want):
        failures.append(f"{label}: 结果数 {len(got)} != 用例数 {len(want)}")


def main():
    argv = sys.argv[1:]
    use_java = "--no-java" not in argv and shutil.which("javac") and shutil.which("java")
    only = {a for a in argv if not a.startswith("--")}

    problems = []
    for path in sorted((ROOT / "problems").glob("*.md")):
        key = path.stem.split("-")[0].lstrip("0")
        if only and key not in only:
            continue
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        problems.append((key, meta, code_blocks(body)))

    failures, missing, java_jobs = [], [], {}
    counts = {"python": 0, "java": 0}
    work = Path(tempfile.mkdtemp(prefix="ct100-"))
    for key, meta, blocks in problems:
        spec = CASES.get(key)
        if not spec:
            missing.append(key)
            continue
        java_srcs = [src for lang, src in blocks if lang == "java"]
        sig = None
        if spec["kind"] == "fn":
            sig = next(filter(None, (java_signature(s, spec["name"]) for s in java_srcs)), None)
        tested = {"python": 0, "java": 0}
        for idx, (lang, src) in enumerate(blocks):
            label = f"[{key}] {lang} 第 {idx + 1} 段"
            if lang == "python":
                try:
                    got = run_python(src, spec, sig)
                except Exception as e:  # noqa: BLE001
                    failures.append(f"{label}: 抛异常 {type(e).__name__}: {e}")
                    tested["python"] += 1
                    continue
                if got is not None:
                    tested["python"] += 1
                    compare(label, got, spec, failures)
            elif lang == "java" and use_java:
                pkg = f"t{re.sub(r'[^0-9a-zA-Z]', '_', key)}_{idx}"
                main_src = java_main(pkg, src, spec)
                if main_src:
                    tested["java"] += 1
                    (work / pkg).mkdir()
                    public = re.search(r"^public\s+class\s+(\w+)", src, re.M)
                    (work / pkg / f"{public[1] if public else 'Code'}.java").write_text(
                        f"package {pkg};\nimport java.util.*;\nimport lc.*;\n{src}\n", encoding="utf-8")
                    (work / pkg / "Main.java").write_text(main_src, encoding="utf-8")
                    java_jobs[pkg] = (label, spec)
        for lang in ("python", "java"):
            counts[lang] += tested[lang]
            if tested[lang] == 0 and (lang == "python" or use_java):
                failures.append(f"[{key}] 没有找到可测的 {lang} 代码")

    if java_jobs:
        (work / "lc").mkdir()
        for name, src in JAVA_LC.items():
            (work / "lc" / name).write_text(src, encoding="utf-8")
        calls = "\n".join(f"        {pkg}.Main.run();" for pkg in java_jobs)
        (work / "Runner.java").write_text(
            f"public class Runner {{\n    public static void main(String[] a) {{\n{calls}\n    }}\n}}\n", encoding="utf-8")
        files = [str(p.relative_to(work)) for p in work.rglob("*.java")]
        proc = subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-d", "out", *files],
                              cwd=work, capture_output=True, text=True)
        if proc.returncode:
            failures.append("javac 编译失败：\n" + proc.stderr.strip())
        else:
            proc = subprocess.run(["java", "-Xss16m", "-cp", "out", "Runner"], cwd=work, capture_output=True, text=True)
            results = {}
            for line in proc.stdout.splitlines():
                if line.startswith("R\t"):
                    _, pkg, idx, val = line.split("\t", 3)
                    results.setdefault(pkg, {})[int(idx)] = json.loads(val)
            if proc.returncode:
                failures.append("java 运行失败：\n" + proc.stderr.strip()[-2000:])
            for pkg, (label, spec) in java_jobs.items():
                got = results.get(pkg, {})
                compare(label, [got.get(i, "!无输出") for i in range(len(expected_of(spec)))], spec, failures)
    shutil.rmtree(work, ignore_errors=True)

    print(f"题目 {len(problems)}，Python 代码段 {counts['python']}，Java 代码段 {counts['java']}"
          + ("" if use_java else "（未跑 Java）"))
    if missing:
        print("没有用例：" + " ".join(missing))
    for f in failures:
        print("FAIL " + f)
    print("全部通过" if not failures else f"{len(failures)} 处失败")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
