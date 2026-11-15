#!/usr/bin/env python3
"""生成复习页面。

    python3 scripts/build.py

读取 problems/*.md 和 libs.md，输出：
  - index.html  单文件页面（数据内嵌，双击即可打开，也可直接挂 GitHub Pages）
                progress.json 若存在，会作为掌握程度的初始值一起嵌进去
  - README.md   刷新 <!-- LIST:START --> 与 <!-- LIST:END --> 之间的题目总表

只用标准库。支持的 Markdown 子集：标题、列表（可嵌套）、代码块、行内代码、
加粗、链接、引用、段落。相邻的 python / java 代码块会合并成可切换的一组。
"""
import html
import io
import json
import keyword
import re
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_NAMES = {"python": "Python", "java": "Java"}


# ---------------------------------------------------------------- 解析

def parse_front_matter(text):
    """返回 (meta, body)。front matter 只支持 `key: value` 和 `key: [a, b]`。"""
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, body.strip("\n")


def code_blocks(md):
    """[(lang, source), ...]"""
    return [(m[1].strip().lower(), m[2])
            for m in re.finditer(r"^```(\w*)[^\n]*\n(.*?)^```", md, re.S | re.M)]


# ---------------------------------------------------------------- 代码高亮

def _wrap(cls, text):
    return f'<span class="{cls}">{html.escape(text)}</span>'


def highlight_python(src):
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError):
        return html.escape(src)
    starts = [0]
    for line in src.split("\n"):
        starts.append(starts[-1] + len(line) + 1)
    out, pos, prev = [], 0, ""
    for tok in tokens:
        name = tokenize.tok_name[tok.type]
        cls = None
        if name == "COMMENT":
            cls = "c"
        elif name == "STRING" or name.startswith("FSTRING"):
            cls = "s"
        elif name == "NUMBER":
            cls = "n"
        elif name == "NAME":
            if keyword.iskeyword(tok.string):
                cls = "k"
            elif prev in ("def", "class"):
                cls = "f"
        if tok.string.strip():
            prev = tok.string
        if not cls:
            continue
        a = starts[tok.start[0] - 1] + tok.start[1]
        b = starts[tok.end[0] - 1] + tok.end[1]
        if a < pos or b > len(src):
            continue
        out.append(html.escape(src[pos:a]))
        out.append(_wrap(cls, src[a:b]))
        pos = b
    out.append(html.escape(src[pos:]))
    return "".join(out)


JAVA_KEYWORDS = set("""abstract assert boolean break byte case catch char class
continue default do double else enum extends final finally float for if
implements import instanceof int interface long new null package private
protected public return short static super switch this throw throws true false
try var void while""".split())
JAVA_TOKEN = re.compile(
    r"(?P<c>//[^\n]*|/\*.*?\*/)"
    r"|(?P<s>\"(?:\\.|[^\"\\\n])*\"|'(?:\\.|[^'\\\n])*')"
    r"|(?P<n>\b\d[\d_]*(?:\.\d+)?[LlFfDd]?\b)"
    r"|(?P<w>\b[A-Za-z_]\w*\b)", re.S)


def highlight_java(src):
    out, pos = [], 0
    for m in JAVA_TOKEN.finditer(src):
        kind, text = m.lastgroup, m.group()
        if kind == "w":
            if text in JAVA_KEYWORDS:
                kind = "k"
            elif text[0].isupper() and not text.isupper():
                kind = "t"
            else:
                continue
        out.append(html.escape(src[pos:m.start()]))
        out.append(_wrap(kind, text))
        pos = m.end()
    out.append(html.escape(src[pos:]))
    return "".join(out)


HIGHLIGHTERS = {"python": highlight_python, "java": highlight_java}


# ---------------------------------------------------------------- Markdown

def inline(text):
    codes = []

    def stash(m):                       # 先把行内代码换成占位符，加粗里就可以包含代码
        codes.append(f"<code>{html.escape(m[1])}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m[1])], text)


def _link(m):
    href = m[2]
    attrs = "" if href.startswith("#") else ' target="_blank" rel="noopener"'
    return f'<a href="{html.escape(href)}"{attrs}>{m[1]}</a>'


LIST_ITEM = re.compile(r"^(\s*)(?:[-*]|(\d+)\.)\s+(.*)$")
FENCE = re.compile(r"^```(\w*)")


def _read_fence(lines, i):
    lang = FENCE.match(lines[i])[1].lower()
    j = i + 1
    while j < len(lines) and not lines[j].startswith("```"):
        j += 1
    return lang, "\n".join(lines[i + 1:j]), j + 1


def _render_code_group(lines, i):
    """从第 i 行的代码块开始，吞掉紧邻的其它语言代码块，合成一组。"""
    blocks = []
    while True:
        lang, src, i = _read_fence(lines, i)
        blocks.append((lang, src))
        j = i
        while j < len(lines) and not lines[j].strip():
            j += 1
        m = FENCE.match(lines[j]) if j < len(lines) else None
        if not m or not m[1] or m[1].lower() in [b[0] for b in blocks]:
            break
        i = j
    pres = []
    for lang, src in blocks:
        body = HIGHLIGHTERS.get(lang, html.escape)(src)
        pres.append(f'<pre data-lang="{lang}"><code>{body}</code></pre>')
    if len(blocks) == 1:
        return f'<div class="code">{pres[0]}</div>', i
    tabs = "".join(
        f'<button type="button" data-set-lang="{lang}">{LANG_NAMES.get(lang, lang)}</button>'
        for lang, _ in blocks)
    return f'<div class="code multi"><div class="langs">{tabs}</div>{"".join(pres)}</div>', i


def _render_list(lines, i):
    out, stack = [], []
    while i < len(lines):
        m = LIST_ITEM.match(lines[i])
        if not m:
            break
        indent, tag = len(m[1]), "ol" if m[2] else "ul"
        while stack and indent < stack[-1][0]:
            out.append(f"</li></{stack.pop()[1]}>")
        if not stack or indent > stack[-1][0]:
            out.append(f"<{tag}>")
            stack.append((indent, tag))
        else:
            out.append("</li>")
        out.append(f"<li>{inline(m[3])}")
        i += 1
    while stack:
        out.append(f"</li></{stack.pop()[1]}>")
    return "".join(out), i


def render_markdown(md, heading_attrs=None):
    """heading_attrs(level, text) 可返回要加到标题标签上的属性字符串。"""
    lines = md.strip("\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("<!--"):
            i += 1
        elif FENCE.match(line):
            block, i = _render_code_group(lines, i)
            out.append(block)
        elif m := re.match(r"^(#{1,4})\s+(.*)$", line):
            level, text = len(m[1]), m[2].strip()
            attrs = heading_attrs(level, text) if heading_attrs else ""
            out.append(f"<h{level}{attrs or ''}>{inline(text)}</h{level}>")
            i += 1
        elif LIST_ITEM.match(line):
            block, i = _render_list(lines, i)
            out.append(block)
        elif line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i][1:].strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
        else:
            para = []
            while (i < len(lines) and lines[i].strip() and not FENCE.match(lines[i])
                   and not re.match(r"^(#{1,4}\s|>)", lines[i]) and not LIST_ITEM.match(lines[i])):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- 数据

def load_problems():
    problems = []
    for path in sorted((ROOT / "problems").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        problems.append({
            "key": path.stem.split("-")[0].lstrip("0"),
            "file": f"problems/{path.name}",
            "rank": int(meta["rank"]),
            "id": str(meta["id"]),
            "title": meta["title"],
            "difficulty": meta["difficulty"],
            "tags": meta.get("tags", []),
            "freq": int(meta.get("freq", 0)),
            "link": meta["link"],
            "desc": meta.get("desc", ""),
            "body": body,
        })
    problems.sort(key=lambda p: p["rank"])
    return problems


def load_libs():
    """libs.md：`## 语言` 下每个 `### 标题` 是一节；
    紧跟标题的 `<!-- match: 正则 -->` 用来在同语言的题目代码里识别「用到了这个库」，
    没有这行注释的小节不参与关联。"""
    path = ROOT / "libs.md"
    if not path.exists():
        return "", []
    text = path.read_text(encoding="utf-8")
    sections, lang = [], ""
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        if m := re.match(r"^##\s+(.*)$", line):
            lang = m[1].strip().lower()
        elif m := re.match(r"^###\s+(.*)$", line):
            match = None
            for nxt in lines[idx + 1:idx + 3]:
                if mm := re.match(r"\s*<!--\s*match:\s*(.+?)\s*-->", nxt):
                    match = re.compile(mm[1])
            title = m[1].strip()
            name = re.sub(r"`", "", re.split(r"\s+[—-]\s+|：|\s*（", title)[0]).strip()
            sections.append({
                "id": f"{lang}-{len(sections)}", "lang": lang, "name": name,
                "title": title, "match": match, "used": [],
            })
    return text, sections


def attach_libs(problems, sections):
    for p in problems:
        used = []
        blocks = code_blocks(p["body"])
        for sec in sections:
            if not sec["match"]:
                continue
            if any(lang == sec["lang"] and sec["match"].search(src) for lang, src in blocks):
                used.append(sec["id"])
                sec["used"].append(p)
        p["libs"] = used


def render_libs(text, sections):
    by_title = {(s["lang"], s["title"]): s for s in sections}
    state = {"lang": ""}

    def attrs(level, heading):
        if level == 2:
            state["lang"] = heading.lower()
            return f' id="lib-{state["lang"]}"'
        if level == 3:
            sec = by_title.get((state["lang"], heading))
            return f' id="lib-{sec["id"]}"' if sec else ""
        return ""

    # 在每节末尾追加「相关题目」
    out, cur, lang = [], None, ""

    def flush():
        if cur and cur["used"]:
            links = " · ".join(f'[{p["id"]}](#/{p["key"]})' for p in cur["used"])
            out.extend(["", f"相关题目：{links}", ""])

    for line in text.split("\n"):
        if re.match(r"^#{1,3}\s", line):
            flush()
            cur = None
            if m := re.match(r"^##\s+(.*)$", line):
                lang = m[1].strip().lower()
            elif m := re.match(r"^###\s+(.*)$", line):
                cur = by_title.get((lang, m[1].strip()))
        out.append(line)
    flush()
    return render_markdown("\n".join(out), attrs)


def load_seed():
    """progress.json：仓库里保存的掌握程度，作为页面的初始值（浏览器里的标记会覆盖它）。"""
    path = ROOT / "progress.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("progress", {})


# ---------------------------------------------------------------- 输出

def build_readme(problems):
    path = ROOT / "README.md"
    if not path.exists():
        return
    rows = ["| # | 题目 | 难度 | 分类 | 原题 |", "|--:|---|---|---|---|"]
    for p in problems:
        rows.append(
            f'| {p["rank"]} | [{p["id"]}. {p["title"]}]({p["file"]}) | {p["difficulty"]} '
            f'| {" · ".join(p["tags"])} | [LeetCode]({p["link"]}) |')
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- LIST:START -->).*?(<!-- LIST:END -->)",
                 lambda m: m[1] + "\n" + "\n".join(rows) + "\n" + m[2], text, flags=re.S)
    if new != text:
        path.write_text(new, encoding="utf-8")


def main():
    problems = load_problems()
    libs_text, sections = load_libs()
    attach_libs(problems, sections)
    data = {
        "problems": [
            {k: p[k] for k in ("key", "rank", "id", "title", "difficulty", "tags",
                               "freq", "link", "desc", "libs")}
            | {"html": render_markdown(p["body"])}
            for p in problems
        ],
        "libs": {
            "html": render_libs(libs_text, sections),
            "sections": [{k: s[k] for k in ("id", "lang", "name")} for s in sections],
        },
        "seed": load_seed(),
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    (ROOT / "index.html").write_text(template.replace("/*__DATA__*/null", payload), encoding="utf-8")
    build_readme(problems)
    print(f"index.html: {len(problems)} 题, {len(sections)} 个常用库条目")


if __name__ == "__main__":
    main()
