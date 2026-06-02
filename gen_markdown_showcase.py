#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_markdown_showcase.py
生成一个 10000+ 行的 Markdown 文件 markdown_showcase.md，覆盖：
- YAML Frontmatter
- 全部常见 Markdown 语法（CommonMark + GFM 扩展）
- 各类特殊字符 / Unicode / Emoji / 数学公式
- 多种 Mermaid 图（flowchart, sequence, class, state, er, gantt, pie, journey, gitGraph, timeline, mindmap, quadrant, sankey, requirement, c4）
- 大量循环展开样例确保 >= 10000 行
"""
import re
from pathlib import Path

OUT = Path(__file__).parent / "markdown_showcase.md"

def to_anchor(heading: str) -> str:
    """
    把标题文字转成 GitHub / CommonMark 标准锚点 ID：
    1. 全部小写
    2. 空格 → -
    3. 删除不允许的字符（保留字母、数字、中文、emoji、- 和 _）
    """
    s = heading.lower()
    s = s.replace(" ", "-")
    # 保留：unicode字母/数字/中文/emoji（\w），以及 - _
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)
    # 连续多个 - 合并
    s = re.sub(r"-{2,}", "-", s)
    s = s.strip("-")
    return s

L = []  # 行缓冲
def w(s=""):
    if isinstance(s, str):
        L.append(s)
    else:
        L.extend(s)

# ============================================================
# 1) YAML Frontmatter
# ============================================================
w("---")
w('title: "Markdown 全语法 & Mermaid 大全 (Markdown Showcase)"')
w('subtitle: "A 10,000+ line stress test for parsers, renderers and your scroll wheel"')
w("author:")
w("  name: CodeBuddy")
w("  email: codebuddy@example.com")
w("  affiliations:")
w("    - Tencent")
w("    - Open Source Community")
w("date: 2026-05-27")
w("version: 1.0.0")
w("language: zh-CN")
w("tags: [markdown, mermaid, yaml, showcase, demo, unicode, emoji]")
w("categories:")
w("  - documentation")
w("  - reference")
w("keywords:")
w("  - Markdown")
w("  - CommonMark")
w("  - GFM")
w("  - Mermaid")
w("  - YAML")
w("description: >")
w("  本文件用于测试 Markdown 解析器与渲染器对 CommonMark、GitHub Flavored Markdown、")
w("  数学公式 (KaTeX/MathJax)、YAML Frontmatter、Mermaid 图表、HTML 嵌入、Unicode")
w("  及 emoji 的完整支持，文件总行数超过 10000 行。")
w("toc: true")
w("toc_depth: 4")
w("math: true")
w("mermaid: true")
w("draft: false")
w("featured_image: /images/cover.png")
w("cover:")
w("  image: /images/cover.png")
w("  alt: cover image")
w("  caption: '封面图（占位）'")
w("license: CC-BY-4.0")
w("permalink: /docs/markdown-showcase/")
w("aliases:")
w("  - /docs/md-everything/")
w("  - /test/markdown-bigfile/")
w("metadata:")
w("  generator: gen_markdown_showcase.py")
w("  build_id: 0xDEADBEEF")
w("  pi: 3.141592653589793")
w("  pages_estimate: 250")
w("  flags:")
w("    experimental: true")
w("    stable: false")
w("  matrix:")
w("    - [1, 2, 3]")
w("    - [4, 5, 6]")
w("    - [7, 8, 9]")
w("---")
w()

# ============================================================
# 2) 目录 / 介绍
# ============================================================
w("# Markdown 全语法 & Mermaid 大全 📚")
w()
w("> 这是一个**超大**的 Markdown 示例文件，用于全面演示 Markdown 各种语法、特殊字符、")
w("> Unicode、emoji 以及 Mermaid 图表。文件总行数 **超过 10,000 行**，可用于压测解析器、")
w("> 编辑器（VS Code / Obsidian / Typora）、静态站点生成器（Hexo / Hugo / Jekyll / MkDocs）")
w("> 与 GitHub / GitLab 的 Markdown 渲染管线。")
w()
w("![status](https://img.shields.io/badge/markdown-showcase-blue)")
w("![lines](https://img.shields.io/badge/lines-10000%2B-success)")
w("![mermaid](https://img.shields.io/badge/mermaid-ready-ff69b4)")
w()
w("---")
w()
w("## 目录")
w()
toc = [
    "1. 标题层级",
    "2. 段落与换行",
    "3. 强调（粗体 / 斜体 / 删除线 / 下划线 / 高亮）",
    "4. 列表（有序 / 无序 / 任务 / 嵌套）",
    "5. 引用块",
    "6. 代码（行内 / 围栏 / 多语言）",
    "7. 链接与图片",
    "8. 表格（基础 / 对齐 / 复杂）",
    "9. 水平分隔线",
    "10. 转义字符与特殊符号",
    "11. HTML 嵌入",
    "12. 数学公式（KaTeX / MathJax）",
    "13. 脚注",
    "14. 定义列表",
    "15. 缩写",
    "16. 高亮 / 上下标",
    "17. Emoji & Unicode 大全",
    "18. Mermaid 图表大全",
    "19. 代码示例集（多语言）",
    "20. 巨型语法循环演示（≥ 10000 行）",
]
for item in toc:
    # 目录对应的实际二级标题是 "## X. 标题"
    anchor = to_anchor(item)
    w(f"- [{item}](#{anchor})")
w()
w("---")
w()

# ============================================================
# 3) 标题层级
# ============================================================
w("## 1. 标题层级")
w()
for i in range(1, 7):
    w(f"{'#'*i} H{i} 标题示例 / Heading level {i}")
w()
w("Setext 风格标题：")
w()
w("一级标题（H1）")
w("==============")
w()
w("二级标题（H2）")
w("--------------")
w()
w("---")
w()

# ============================================================
# 4) 段落与换行
# ============================================================
w("## 2. 段落与换行")
w()
w("这是一个普通段落。Markdown 中段落由 **空行** 分隔。")
w()
w("这是另一个段落。  ")  # 行尾两空格 = 硬换行
w("这一行使用了「行尾两个空格」实现硬换行。")
w()
w("也可以使用反斜杠 \\\n实现硬换行（部分解析器支持）。")
w()
w("---")
w()

# ============================================================
# 5) 强调
# ============================================================
w("## 3. 强调")
w()
w("- *斜体（单星号）* 或 _斜体（单下划线）_")
w("- **粗体（双星号）** 或 __粗体（双下划线）__")
w("- ***粗斜体*** 或 ___粗斜体___")
w("- ~~删除线~~（GFM）")
w("- ==高亮==（部分渲染器支持，如 Obsidian / Typora）")
w("- <u>下划线（依赖 HTML）</u>")
w("- `行内代码`")
w("- H~2~O 下标 / X^2^ 上标（部分渲染器支持）")
w()
w("---")
w()

# ============================================================
# 6) 列表
# ============================================================
w("## 4. 列表")
w()
w("### 4.1 无序列表")
w("- 苹果 🍎")
w("- 香蕉 🍌")
w("  - 嵌套 1")
w("    - 嵌套 2")
w("      - 嵌套 3")
w("        - 嵌套 4")
w("- 樱桃 🍒")
w()
w("使用 `*` 或 `+`：")
w("* item-a")
w("+ item-b")
w()
w("### 4.2 有序列表")
for i in range(1, 11):
    w(f"{i}. 第 {i} 项")
w()
w("### 4.3 任务列表（GFM）")
w("- [x] 写文档")
w("- [x] 加 Mermaid 图")
w("- [ ] 加测试用例")
w("- [ ] 校对 1 万行内容")
w("  - [x] 自动生成脚本")
w("  - [ ] 人工抽样审阅")
w()
w("### 4.4 嵌套混合")
w("1. 一级有序")
w("   - 二级无序")
w("     1. 三级有序")
w("        - 四级无序")
w("          - [ ] 五级任务")
w()
w("---")
w()

# ============================================================
# 7) 引用块
# ============================================================
w("## 5. 引用块")
w()
w("> 单层引用。Markdown 真好用。")
w(">")
w("> > 二层嵌套引用。引用中也可以使用 **强调** 与 `代码`。")
w(">")
w("> > > 三层嵌套：> > > 像俄罗斯套娃 🪆。")
w()
w("> **注意**：GitHub / Obsidian 支持 callout / alert 语法：")
w()
w("> [!NOTE]")
w("> 这是一条 NOTE 提示。")
w()
w("> [!TIP]")
w("> 这是一条 TIP 小贴士。")
w()
w("> [!IMPORTANT]")
w("> 这是一条 IMPORTANT 提示。")
w()
w("> [!WARNING]")
w("> 这是一条 WARNING 警告。")
w()
w("> [!CAUTION]")
w("> 这是一条 CAUTION 严重警告。")
w()
w("---")
w()

# ============================================================
# 8) 代码
# ============================================================
w("## 6. 代码")
w()
w("行内：`const x = 42;`，转义反引号 `` ` ``，多反引号 ``` `` 包裹 ``` 同样有效。")
w()
w("缩进式代码块（每行 4 空格）：")
w()
w("    function hello() {")
w("      console.log('hello');")
w("    }")
w()
w("围栏代码块（带语言标识）：")
w()
fenced_samples = {
    "python": '''# Python 示例
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print([fib(i) for i in range(10)])''',

    "javascript": '''// JavaScript 示例
const fib = n => {
  let [a, b] = [0n, 1n];
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  return a;
};
console.log(Array.from({length:10}, (_,i) => fib(i)));''',

    "typescript": '''// TypeScript 示例
type Pair<T> = readonly [T, T];
const swap = <T>([a, b]: Pair<T>): Pair<T> => [b, a] as const;
console.log(swap([1, 2]));''',

    "go": '''// Go 示例
package main
import "fmt"
func main() {
    a, b := 0, 1
    for i := 0; i < 10; i++ {
        fmt.Println(a)
        a, b = b, a+b
    }
}''',

    "rust": '''// Rust 示例
fn fib(n: u32) -> u128 {
    let (mut a, mut b) = (0u128, 1u128);
    for _ in 0..n { let t = a; a = b; b = t + b; }
    a
}
fn main() { for i in 0..10 { println!("{}", fib(i)); } }''',

    "java": '''// Java 示例
public class Fib {
    public static void main(String[] args) {
        long a = 0, b = 1;
        for (int i = 0; i < 10; i++) {
            System.out.println(a);
            long t = a; a = b; b = t + b;
        }
    }
}''',

    "cpp": '''// C++ 示例
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long a=0,b=1;
    for (int i=0;i<10;i++) { cout<<a<<"\\n"; tie(a,b)=make_tuple(b,a+b); }
}''',

    "c": '''/* C 示例 */
#include <stdio.h>
int main(void){ long a=0,b=1; for(int i=0;i<10;i++){ printf("%ld\\n",a); long t=a; a=b; b=t+b; } }''',

    "csharp": '''// C# 示例
using System;
class Program {
    static void Main() {
        long a = 0, b = 1;
        for (int i = 0; i < 10; i++) {
            Console.WriteLine(a);
            (a, b) = (b, a + b);
        }
    }
}''',

    "kotlin": '''// Kotlin 示例
fun fib(n: Int): Long {
    var a = 0L; var b = 1L
    repeat(n) { val t = a; a = b; b = t + b }
    return a
}
fun main() = (0..9).forEach { println(fib(it)) }''',

    "swift": '''// Swift 示例
func fib(_ n: Int) -> Int {
    var (a,b) = (0,1)
    for _ in 0..<n { (a,b) = (b,a+b) }
    return a
}
print((0..<10).map(fib))''',

    "ruby": '''# Ruby 示例
def fib(n); a,b = 0,1; n.times { a,b = b,a+b }; a; end
puts (0...10).map { |i| fib(i) }.join(", ")''',

    "php": '''<?php
function fib($n) { $a=0;$b=1; for($i=0;$i<$n;$i++) { [$a,$b]=[$b,$a+$b]; } return $a; }
for ($i=0;$i<10;$i++) echo fib($i)."\\n";''',

    "bash": '''#!/usr/bin/env bash
# Bash 示例
a=0; b=1
for i in $(seq 1 10); do
  echo "$a"
  a_new=$b
  b=$((a + b))
  a=$a_new
done''',

    "sql": '''-- SQL 示例（PostgreSQL 递归 CTE 生成斐波那契）
WITH RECURSIVE fib(i, a, b) AS (
  SELECT 1, 0::bigint, 1::bigint
  UNION ALL
  SELECT i+1, b, a+b FROM fib WHERE i < 10
)
SELECT i, a AS fib_n FROM fib;''',

    "yaml": '''# YAML 示例
server:
  host: 0.0.0.0
  port: 8080
  tls:
    enabled: true
    cert: /etc/ssl/server.pem
features: [auth, cache, metrics]''',

    "toml": '''# TOML 示例
[server]
host = "0.0.0.0"
port = 8080
[server.tls]
enabled = true
cert = "/etc/ssl/server.pem"
[features]
list = ["auth", "cache", "metrics"]''',

    "json": '''{
  "name": "showcase",
  "version": "1.0.0",
  "deps": ["mermaid", "katex"],
  "config": { "math": true, "mermaid": true }
}''',

    "xml": '''<?xml version="1.0" encoding="UTF-8"?>
<config>
  <server host="0.0.0.0" port="8080">
    <tls enabled="true" cert="/etc/ssl/server.pem"/>
  </server>
</config>''',

    "html": '''<!DOCTYPE html>
<html lang="zh-CN">
  <head><meta charset="UTF-8"><title>Hello</title></head>
  <body><h1>Hello, World!</h1></body>
</html>''',

    "css": '''/* CSS 示例 */
:root { --primary: #1a73e8; }
.btn { color: var(--primary); transition: transform .2s; }
.btn:hover { transform: scale(1.05); }''',

    "scss": '''// SCSS 示例
$primary: #1a73e8;
.btn {
  color: $primary;
  &:hover { transform: scale(1.05); }
}''',

    "dockerfile": '''# Dockerfile 示例
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]''',

    "makefile": '''# Makefile 示例
.PHONY: build test
build:
\tgo build -o bin/app ./cmd/app
test:
\tgo test ./...''',

    "ini": '''; INI 示例
[server]
host=0.0.0.0
port=8080
[logging]
level=INFO''',

    "diff": '''--- a/file.txt
+++ b/file.txt
@@ -1,3 +1,3 @@
 hello
-world
+world!
 bye''',

    "powershell": '''# PowerShell 示例
$a, $b = 0, 1
1..10 | ForEach-Object {
    Write-Output $a
    $a, $b = $b, ($a + $b)
}''',

    "lua": '''-- Lua 示例
local function fib(n)
  local a, b = 0, 1
  for _ = 1, n do a, b = b, a + b end
  return a
end
for i = 0, 9 do print(fib(i)) end''',

    "r": '''# R 示例
fib <- function(n) {
  a <- 0; b <- 1
  for (i in seq_len(n)) { tmp <- a; a <- b; b <- tmp + b }
  a
}
sapply(0:9, fib)''',

    "haskell": '''-- Haskell 示例
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
main :: IO ()
main = print (take 10 fibs)''',

    "scala": '''// Scala 示例
def fib(n: Int): BigInt = {
  var (a, b) = (BigInt(0), BigInt(1))
  for (_ <- 0 until n) { val t = a; a = b; b = t + b }
  a
}
(0 until 10).map(fib).foreach(println)''',
}
for lang, code in fenced_samples.items():
    w(f"```{lang}")
    for line in code.splitlines():
        w(line)
    w("```")
    w()

w("**带行号 / 高亮（部分渲染器）**：")
w()
w("```python {linenos=true hl_lines=[2,4]}")
w("def add(a, b):")
w("    return a + b           # 高亮行")
w("def sub(a, b):")
w("    return a - b           # 高亮行")
w("```")
w()
w("---")
w()

# ============================================================
# 9) 链接与图片
# ============================================================
w("## 7. 链接与图片")
w()
w("- 内联链接：[CodeBuddy](https://codebuddy.ai)")
w('- 带 title：[GitHub](https://github.com "Where the world builds software")')
w("- 自动链接：<https://example.com> 或 <user@example.com>")
w("- 参考式链接：[Wikipedia][wiki]")
w("- 锚点链接：[跳转到 Mermaid 章节](#18-mermaid-图表大全)")
w('- 同段中带格式的链接：[**粗体**链接](https://example.com)')
w()
w("[wiki]: https://wikipedia.org \"Wikipedia\"")
w()
w("**图片**：")
w()
w("![占位图](https://via.placeholder.com/600x200.png \"placeholder\")")
w()
w("![带链接的图][img1]")
w()
w("[img1]: https://via.placeholder.com/300x100.png \"img-ref\"")
w()
w("**图片 + 链接**：")
w()
w("[![logo](https://via.placeholder.com/120x40.png)](https://example.com)")
w()
w("---")
w()

# ============================================================
# 10) 表格
# ============================================================
w("## 8. 表格")
w()
w("### 8.1 基础表格")
w()
w("| 列 A | 列 B | 列 C |")
w("| ---- | ---- | ---- |")
w("| a1   | b1   | c1   |")
w("| a2   | b2   | c2   |")
w()
w("### 8.2 对齐表格")
w()
w("| 左对齐 | 居中 | 右对齐 |")
w("| :----- | :--: | -----: |")
w("| L      |  C   |      R |")
w("| left   | mid  |  right |")
w()
w("### 8.3 含格式的复杂表格")
w()
w("| 语言 | 示例 | 性能 ⭐ | 备注 |")
w("| :--- | :--- | :----: | :--- |")
w("| **Python** | `print('hi')` | ★★★☆☆ | *动态类型* |")
w("| **Rust**   | `println!()`  | ★★★★★ | ~~GC~~ 无 GC |")
w("| **Go**     | `fmt.Println()` | ★★★★☆ | 并发优秀 |")
w("| HTML 单元格 | <kbd>Ctrl</kbd>+<kbd>C</kbd> | — | <sup>支持</sup> |")
w()
w("### 8.4 长表格（自动生成）")
w()
w("| # | 名称 | 类型 | 取值 | 备注 |")
w("|--:|:-----|:-----|-----:|:-----|")
for i in range(1, 31):
    w(f"| {i} | item-{i:02d} | T{(i%5)+1} | {i*7} | row-{i} |")
w()
w("---")
w()

# ============================================================
# 11) 水平分隔线
# ============================================================
w("## 9. 水平分隔线")
w()
w("---")
w()
w("***")
w()
w("___")
w()
w("- - -")
w()
w("---")
w()

# ============================================================
# 12) 转义与特殊字符
# ============================================================
w("## 10. 转义字符与特殊符号")
w()
w("Markdown 转义：")
w(r"\* \_ \{ \} \[ \] \( \) \# \+ \- \. \! \\ \` \> \| \~")
w()
w("常见特殊字符／全角／半角：")
w("`! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : ' \" , . / < > ? \\ | ` ~ `")
w("中文标点：，。、；：「」『』（）《》〈〉“ ” ‘ ’ ！？……—— ·")
w()
w("HTML 实体：&copy; &reg; &trade; &amp; &lt; &gt; &quot; &nbsp; &hellip; &mdash; &ndash;")
w()
w("常用符号：© ® ™ § ¶ † ‡ • ‣ ◦ ⁂ ※ ☆ ★ ✓ ✗ ✘ ✓ ✔ ✖ ☑ ☒ ☐ ⚠ ⚡ ☀ ☁ ☂ ☃ ⌘ ⌥ ⇧ ⌃ ↩")
w()
w("货币：$ ¥ € £ ₩ ₹ ₽ ₿ ₺ ₪ ₱ ¢")
w("数学：± × ÷ ≠ ≈ ≡ ≤ ≥ ∞ √ ∑ ∏ ∫ ∂ ∇ ∈ ∉ ⊂ ⊃ ∪ ∩ ∅ ∀ ∃ ¬ ∧ ∨ → ← ↔ ⇒ ⇐ ⇔")
w("希腊：α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω Α Β Γ Δ Θ Λ Π Σ Φ Ω")
w("箭头：← → ↑ ↓ ↔ ↕ ⇐ ⇒ ⇑ ⇓ ⇔ ⇕ ↩ ↪ ⤴ ⤵ ➜ ➡ ⬅ ⬆ ⬇")
w("方块：░ ▒ ▓ █ ▌ ▐ ▀ ▄ ■ □ ▣ ▤ ▥ ▦ ▧ ▨ ▩")
w("音乐：♩ ♪ ♫ ♬ ♭ ♮ ♯ 𝄞")
w("棋牌：♠ ♣ ♥ ♦ ♤ ♧ ♡ ♢")
w("骰子：⚀ ⚁ ⚂ ⚃ ⚄ ⚅")
w("天气：☀ ☁ ☂ ☃ ❄ ☔ ⛄ ⛅ ⛈")
w()
w("---")
w()

# ============================================================
# 13) HTML 嵌入
# ============================================================
w("## 11. HTML 嵌入")
w()
w("<div align=\"center\">")
w("  <h3>居中标题（HTML）</h3>")
w("  <p style=\"color:#1a73e8;\">这是一段彩色文字</p>")
w("</div>")
w()
w("<details>")
w("<summary>👉 点击展开/折叠</summary>")
w()
w("- 隐藏内容 1")
w("- 隐藏内容 2")
w("- 隐藏内容 3")
w()
w("```python")
w("print('hello, hidden world')")
w("```")
w()
w("</details>")
w()
w("<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>")
w()
w("<mark>HTML mark 高亮</mark>")
w()
w("<sub>下标</sub> 与 <sup>上标</sup>")
w()
w("<abbr title=\"HyperText Markup Language\">HTML</abbr> 是超文本标记语言。")
w()
w("<blockquote cite=\"https://example.com\">这是一段 HTML 引用。</blockquote>")
w()
w("<table>")
w("  <tr><th>原生</th><th>HTML 表格</th></tr>")
w("  <tr><td>A</td><td>1</td></tr>")
w("  <tr><td>B</td><td>2</td></tr>")
w("</table>")
w()
w("---")
w()

# ============================================================
# 14) 数学公式
# ============================================================
w("## 12. 数学公式（KaTeX / MathJax）")
w()
w("行内公式：当 \\(a \\ne 0\\)，方程 \\(ax^2+bx+c=0\\) 的解为 $x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$。")
w()
w("块级公式：")
w()
w("$$")
w("\\int_{-\\infty}^{\\infty} e^{-x^2}\\,dx = \\sqrt{\\pi}")
w("$$")
w()
w("$$")
w("\\begin{aligned}")
w("\\nabla \\cdot \\mathbf{E} &= \\frac{\\rho}{\\varepsilon_0} \\\\")
w("\\nabla \\cdot \\mathbf{B} &= 0 \\\\")
w("\\nabla \\times \\mathbf{E} &= -\\frac{\\partial \\mathbf{B}}{\\partial t} \\\\")
w("\\nabla \\times \\mathbf{B} &= \\mu_0 \\mathbf{J} + \\mu_0\\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}")
w("\\end{aligned}")
w("$$")
w()
w("矩阵：")
w()
w("$$")
w("A = \\begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\end{bmatrix}")
w("$$")
w()
w("分段函数：")
w()
w("$$")
w("f(x) = \\begin{cases} x^2, & x \\ge 0 \\\\ -x, & x < 0 \\end{cases}")
w("$$")
w()
w("欧拉公式：$e^{i\\pi} + 1 = 0$ — 数学界最美等式。")
w()
w("---")
w()

# ============================================================
# 15) 脚注 / 定义列表 / 缩写
# ============================================================
w("## 13. 脚注")
w()
w("这里是一段带脚注的文字[^1]，也可以引用第二个脚注[^note]。")
w()
w("[^1]: 这是脚注 1 的内容。")
w("[^note]: 这是一个命名脚注，可以包含 **格式** 和 `代码`。")
w()
w("## 14. 定义列表")
w()
w("Markdown")
w(":  一种轻量级标记语言。")
w()
w("Mermaid")
w(":  一种基于文本的图表语法，可以渲染流程图、时序图等。")
w()
w("YAML")
w(":  *YAML Ain't Markup Language*，一种数据序列化格式。")
w()
w("## 15. 缩写")
w()
w("HTML 与 CSS 是 Web 的两块基石。")
w()
w("*[HTML]: HyperText Markup Language")
w("*[CSS]: Cascading Style Sheets")
w()
w("## 16. 高亮 / 上下标")
w()
w("水的化学式：H~2~O；二氧化碳：CO~2~；爱因斯坦质能方程：E = mc^2^。")
w()
w("==这是高亮文本==（部分渲染器）。")
w()
w("---")
w()

# ============================================================
# 16) Emoji & Unicode
# ============================================================
w("## 17. Emoji & Unicode 大全")
w()
emoji_groups = {
    "笑脸 & 表情": "😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 😉 😊 😇 🥰 😍 🤩 😘 😗 ☺️ 😚 😙 🥲 😋 😛 😜 🤪 😝 🤑 🤗 🤭 🤫 🤔 🤐 🤨 😐 😑 😶 😏 😒 🙄 😬 🤥 😌 😔 😪 🤤 😴 😷 🤒 🤕 🤢 🤮 🤧 🥵 🥶 🥴 😵 🤯 🤠 🥳 😎",
    "动物": "🐶 🐱 🐭 🐹 🐰 🦊 🐻 🐼 🐻‍❄️ 🐨 🐯 🦁 🐮 🐷 🐽 🐸 🐵 🙈 🙉 🙊 🐒 🐔 🐧 🐦 🐤 🐣 🐥 🦆 🦅 🦉 🦇 🐺 🐗 🐴 🦄 🐝 🪱 🐛 🦋 🐌 🐞 🐜 🪰 🪲 🪳 🦟 🦗 🕷 🕸 🦂",
    "食物": "🍎 🍐 🍊 🍋 🍌 🍉 🍇 🍓 🫐 🍈 🍒 🍑 🥭 🍍 🥥 🥝 🍅 🍆 🥑 🥦 🥬 🥒 🌶 🫑 🌽 🥕 🫒 🧄 🧅 🥔 🍠 🥐 🥯 🍞 🥖 🥨 🧀 🥚 🍳 🧈 🥞 🧇 🥓 🥩 🍗 🍖",
    "活动": "⚽ 🏀 🏈 ⚾ 🥎 🎾 🏐 🏉 🥏 🎱 🪀 🏓 🏸 🏒 🏑 🥍 🏏 🪃 🥅 ⛳ 🪁 🎣 🤿 🎽 🛹 🛼 🛷 ⛸ 🥌 🎿 ⛷ 🏂 🪂 🏋️ 🤼 🤸 ⛹️ 🤺 🤾 🏌️ 🏇 🧘 🏄 🏊 🚣",
    "旅行": "🚗 🚕 🚙 🚌 🚎 🏎 🚓 🚑 🚒 🚐 🚚 🚛 🚜 🦽 🦼 🛴 🚲 🛵 🏍 🛺 🚨 🚔 🚍 🚘 🚖 🚡 🚠 🚟 🚃 🚋 🚞 🚝 🚄 🚅 🚈 🚂 🚆 🚇 🚊 🚉 ✈️ 🛫 🛬 🛩 💺 🛰 🚀 🛸",
    "对象": "⌚ 📱 📲 💻 ⌨️ 🖥 🖨 🖱 🖲 🕹 🗜 💽 💾 💿 📀 📼 📷 📸 📹 🎥 📽 🎞 📞 ☎️ 📟 📠 📺 📻 🎙 🎚 🎛 🧭 ⏱ ⏲ ⏰ 🕰 ⌛ ⏳ 📡 🔋 🔌 💡 🔦 🕯",
    "符号": "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 💔 ❣️ 💕 💞 💓 💗 💖 💘 💝 💟 ☮️ ✝️ ☪️ 🕉 ☸️ ✡️ 🔯 🕎 ☯️ ☦️ 🛐 ⛎ ♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓ 🆔",
    "国旗": "🇨🇳 🇺🇸 🇯🇵 🇰🇷 🇩🇪 🇫🇷 🇬🇧 🇮🇹 🇪🇸 🇷🇺 🇨🇦 🇦🇺 🇧🇷 🇮🇳 🇲🇽 🇿🇦 🇪🇬 🇹🇷 🇸🇦 🇦🇪 🇸🇬 🇲🇾 🇹🇭 🇻🇳 🇮🇩 🇵🇭 🇳🇿 🇨🇭 🇸🇪 🇳🇴 🇫🇮 🇩🇰 🇳🇱 🇧🇪 🇵🇱 🇨🇿 🇦🇹",
}
for k, v in emoji_groups.items():
    w(f"### {k}")
    w(v)
    w()

w("**Unicode 各语种 Hello**：")
w()
hellos = [
    "English: Hello, World!",
    "中文（简体）: 你好，世界！",
    "中文（繁體）: 你好，世界！",
    "日本語: こんにちは、世界！",
    "한국어: 안녕하세요, 세계!",
    "Español: ¡Hola, Mundo!",
    "Français: Bonjour le monde!",
    "Deutsch: Hallo Welt!",
    "Italiano: Ciao, mondo!",
    "Português: Olá, Mundo!",
    "Русский: Привет, мир!",
    "العربية: مرحبا بالعالم!",
    "עברית: שלום עולם!",
    "हिन्दी: नमस्ते दुनिया!",
    "ไทย: สวัสดีชาวโลก!",
    "Tiếng Việt: Xin chào thế giới!",
    "Türkçe: Merhaba Dünya!",
    "Ελληνικά: Γειά σου Κόσμε!",
    "Українська: Привіт, світе!",
    "فارسی: سلام دنیا!",
    "Esperanto: Saluton, mondo!",
    "Latin: Salve, munde!",
]
for h in hellos:
    w(f"- {h}")
w()
w("**特殊空白与不可见字符**：")
w("- 普通空格：`a b`")
w("- 不间断空格（U+00A0）：`a\u00a0b`")
w("- 全角空格（U+3000）：`a\u3000b`")
w("- 零宽空格（U+200B）：`a\u200bb`")
w("- 零宽连接符（U+200D）：👨\u200d👩\u200d👧\u200d👦")
w()
w("---")
w()

# ============================================================
# 17) Mermaid 大全
# ============================================================
w("## 18. Mermaid 图表大全")
w()

mermaid_blocks = {
    "Flowchart (TD)": """flowchart TD
    A([开始]) --> B{条件?}
    B -- 是 --> C[执行 A]
    B -- 否 --> D[执行 B]
    C --> E[结束]
    D --> E
    classDef green fill:#d4f7d4,stroke:#2e7d32;
    class C green""",

    "Flowchart (LR) 子图": """flowchart LR
    subgraph Frontend
        FE1[React] --> FE2[Vite]
    end
    subgraph Backend
        BE1[Go] --> BE2[PostgreSQL]
    end
    FE2 -- HTTP --> BE1""",

    "Sequence Diagram": """sequenceDiagram
    autonumber
    participant U as User
    participant W as Web
    participant API as Server
    participant DB as Database
    U->>W: 打开页面
    W->>API: GET /data
    API->>DB: SELECT * FROM t
    DB-->>API: rows
    API-->>W: JSON
    W-->>U: 渲染
    Note over U,W: 用户看到结果
    loop 每 5 秒
        W->>API: 心跳
        API-->>W: pong
    end""",

    "Class Diagram": """classDiagram
    class Animal {
      +String name
      +int age
      +eat() void
      +sleep() void
    }
    class Dog {
      +bark() void
    }
    class Cat {
      +meow() void
    }
    Animal <|-- Dog
    Animal <|-- Cat
    Dog : +String breed
    Cat : +bool indoor""",

    "State Diagram": """stateDiagram-v2
    [*] --> Idle
    Idle --> Loading : fetch()
    Loading --> Success : 200 OK
    Loading --> Error : 4xx/5xx
    Success --> Idle : reset()
    Error --> Idle : retry()
    Success --> [*]""",

    "ER Diagram": """erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    CUSTOMER {
      string name
      string email
    }
    ORDER {
      int id
      date created_at
    }
    LINE-ITEM {
      int qty
      float price
    }""",

    "Gantt": """gantt
    title 项目排期
    dateFormat  YYYY-MM-DD
    section 设计
    需求分析 :done,    des1, 2026-01-01, 7d
    UI 设计  :active,  des2, after des1, 10d
    section 开发
    前端    :         dev1, after des2, 20d
    后端    :         dev2, after des2, 25d
    section 测试
    联调测试:          t1,   after dev2, 10d
    上线    :milestone, m1,  after t1, 0d""",

    "Pie Chart": """pie title 编程语言使用占比
    "Python" : 32
    "JavaScript" : 28
    "Go" : 14
    "Rust" : 10
    "Java" : 9
    "Other" : 7""",

    "Journey": """journey
    title 用户购买流程
    section 浏览
      打开 App: 5: 用户
      搜索商品: 4: 用户
    section 决策
      查看详情: 4: 用户
      加入购物车: 3: 用户
    section 支付
      提交订单: 2: 用户, 系统
      完成支付: 5: 用户, 系统""",

    "Git Graph": """gitGraph
    commit id: "init"
    commit id: "feat: setup"
    branch dev
    checkout dev
    commit id: "feat: A"
    commit id: "feat: B"
    checkout main
    merge dev tag: "v1.0"
    branch hotfix
    commit id: "fix: bug"
    checkout main
    merge hotfix tag: "v1.0.1" """,

    "Timeline": """timeline
    title 编程语言诞生年表
    1972 : C
    1985 : C++
    1991 : Python
    1995 : Java : JavaScript : PHP
    2000 : C#
    2009 : Go
    2010 : Rust
    2014 : Swift
    2012 : TypeScript""",

    "Mindmap": """mindmap
  root((Markdown))
    语法
      标题
      列表
      表格
      代码
    扩展
      Mermaid
      KaTeX
      Frontmatter
    工具
      VS Code
      Obsidian
      Typora
    输出
      HTML
      PDF
      Slides""",

    "Quadrant Chart": """quadrantChart
    title 任务优先级象限
    x-axis 低紧急 --> 高紧急
    y-axis 低重要 --> 高重要
    quadrant-1 立即处理
    quadrant-2 计划安排
    quadrant-3 暂缓
    quadrant-4 委派
    重构核心模块: [0.7, 0.9]
    修复线上 Bug: [0.95, 0.85]
    学习新框架: [0.2, 0.7]
    回复邮件: [0.6, 0.2]
    整理桌面: [0.1, 0.1]""",

    "Sankey Diagram": """sankey-beta
A,B,5
A,C,10
B,D,7
C,D,3
C,E,4""",

    "Requirement Diagram": """requirementDiagram
    requirement test_req {
      id: 1
      text: 系统应在 200ms 内响应
      risk: high
      verifymethod: test
    }
    element user_login {
      type: feature
    }
    user_login - satisfies -> test_req""",

    "C4 Context": """C4Context
    title 系统上下文
    Person(user, "用户")
    System(sys, "Showcase 系统", "演示用 Web 应用")
    System_Ext(ext, "第三方支付", "支付网关")
    Rel(user, sys, "使用")
    Rel(sys, ext, "调用 API")""",
}

for title, code in mermaid_blocks.items():
    w(f"### {title}")
    w()
    w("```mermaid")
    for line in code.splitlines():
        w(line)
    w("```")
    w()

w("---")
w()

# ============================================================
# 18) 代码示例集（多语言再演示）
# ============================================================
w("## 19. 代码示例集（多语言再演示）")
w()
extra_codes = [
    ("python", "斐波那契生成器", "def fib_gen():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n"),
    ("javascript", "Promise 链", "fetch('/api')\n  .then(r => r.json())\n  .then(d => console.log(d))\n  .catch(e => console.error(e));\n"),
    ("typescript", "泛型函数", "function identity<T>(x: T): T { return x; }\nconst n = identity<number>(42);\n"),
    ("rust", "trait + impl", "trait Greet { fn hi(&self) -> String; }\nstruct W; impl Greet for W { fn hi(&self) -> String { \"hi\".into() } }\n"),
    ("go", "goroutine", "go func(){ for i := 0; i < 3; i++ { fmt.Println(i) } }()\n"),
    ("java", "Stream API", "list.stream().filter(x -> x > 0).mapToInt(Integer::intValue).sum();\n"),
    ("kotlin", "data class", "data class User(val name: String, val age: Int)\n"),
    ("swift", "optional chaining", "let len = user?.name?.count ?? 0\n"),
    ("c", "指针", "int x = 10; int *p = &x; printf(\"%d\\n\", *p);\n"),
    ("cpp", "lambda", "auto add = [](int a, int b){ return a + b; };\n"),
    ("ruby", "block", "[1,2,3].each { |x| puts x * x }\n"),
    ("php", "数组解构", "[$a, $b] = [1, 2];\n"),
    ("bash", "循环", "for f in *.md; do echo \"$f\"; done\n"),
    ("sql", "JOIN", "SELECT u.id, COUNT(o.id) FROM users u LEFT JOIN orders o ON o.uid=u.id GROUP BY u.id;\n"),
    ("haskell", "map", "map (*2) [1..5] -- [2,4,6,8,10]\n"),
    ("scala", "case class", "case class Point(x: Int, y: Int)\n"),
    ("r", "向量化", "x <- 1:10; mean(x); sd(x)\n"),
    ("lua", "table", "local t = {1,2,3}; for i,v in ipairs(t) do print(i,v) end\n"),
    ("powershell", "管道", "Get-Process | Where-Object { $_.CPU -gt 100 } | Sort-Object CPU -Descending\n"),
]
for lang, desc, code in extra_codes:
    w(f"**{desc} — `{lang}`**")
    w()
    w(f"```{lang}")
    for line in code.splitlines():
        w(line)
    w("```")
    w()

w("---")
w()

# ============================================================
# 19) 巨型循环演示，把行数撑到 10000+
# ============================================================
w("## 20. 巨型语法循环演示（≥ 10000 行）")
w()
w("> 以下小节通过循环展开多个语法块来确保整个文档行数超过 10,000 行；")
w("> 每个小节都用不同的 Markdown 语法组合展示，并间隔插入 Mermaid 图表。")
w()

# 一个完整的「样本块」：标题 + 段落 + 表格 + 代码 + 列表 + 引用 + Mermaid
def emit_sample_block(i: int):
    w(f"### 20.{i} 样本块 #{i} — 综合演示")
    w()
    w(f"这是第 **{i}** 个样本块，用于演示 *Markdown* 在大文档下的解析稳定性。"
      f"包含粗体、斜体、`行内代码`、~~删除线~~、[链接](https://example.com/{i}) 与 emoji 🚀。")
    w()
    w("#### 列表")
    w(f"- 项目 A-{i}")
    w(f"- 项目 B-{i}")
    w(f"  - 子项 B1-{i}")
    w(f"  - 子项 B2-{i}")
    w(f"- 项目 C-{i}")
    w(f"1. 步骤 1 of block {i}")
    w(f"2. 步骤 2 of block {i}")
    w(f"3. 步骤 3 of block {i}")
    w("- [x] 已完成的任务")
    w("- [ ] 待办任务")
    w()
    w("#### 表格")
    w("| ID | 名称 | 状态 | 描述 |")
    w("|---:|:----|:---:|:-----|")
    for k in range(1, 5):
        status = ["OK", "WARN", "FAIL", "INFO"][k % 4]
        w(f"| {i*10+k} | item-{i}-{k} | {status} | 描述-{i}-{k} |")
    w()
    w("#### 代码")
    w("```python")
    w(f"# block #{i}")
    w(f"def handler_{i}(x):")
    w(f"    return x * {i} + {i**2}")
    w(f"print(handler_{i}({i}))")
    w("```")
    w()
    w("#### 引用")
    w(f"> 这是块 #{i} 中的引用文本。")
    w(f"> > 嵌套引用：value = {i*7}")
    w()
    # 每 5 个块插一个 mermaid 图
    if i % 5 == 0:
        w("#### Mermaid 流程图")
        w("```mermaid")
        w("flowchart LR")
        w(f"    S{i}([Start #{i}]) --> P{i}{{Process?}}")
        w(f"    P{i} -- yes --> A{i}[Do A]")
        w(f"    P{i} -- no  --> B{i}[Do B]")
        w(f"    A{i} --> E{i}([End])")
        w(f"    B{i} --> E{i}")
        w("```")
        w()
    # 每 7 个块插入数学公式
    if i % 7 == 0:
        w("#### 数学公式")
        w("$$")
        w(f"f_{{{i}}}(x) = \\sum_{{k=1}}^{{{i}}} \\frac{{x^k}}{{k!}}")
        w("$$")
        w()
    # 每 11 个块插入定义列表
    if i % 11 == 0:
        w("#### 定义")
        w(f"Term-{i}")
        w(f":  这是第 {i} 个术语的定义。包含 *斜体* 与 **粗体**。")
        w()
    # 每 13 个块插入折叠块
    if i % 13 == 0:
        w("<details>")
        w(f"<summary>📦 折叠详情 #{i}</summary>")
        w()
        w(f"隐藏内容 — 块 {i}")
        w()
        w("```bash")
        w(f"echo 'hidden-{i}'")
        w("```")
        w()
        w("</details>")
        w()
    w("---")
    w()

# 一个块大约 35~55 行，跑 280 个块即可超过 10000 行
NUM_BLOCKS = 280
for i in range(1, NUM_BLOCKS + 1):
    emit_sample_block(i)

# ============================================================
# 收尾
# ============================================================
w("## 结尾")
w()
w("如果你滚到了这里，恭喜你 🎉 已经看完了一个超过 10,000 行的 Markdown 大全。")
w()
w("```text")
w("                                ┌──────────────────────────┐")
w("                                │   THE END / 完           │")
w("                                └──────────────────────────┘")
w("```")
w()
w("> *— Generated by `gen_markdown_showcase.py`*")
w()

# ============================================================
# 写入文件
# ============================================================
text = "\n".join(L) + "\n"
OUT.write_text(text, encoding="utf-8")
line_count = text.count("\n")
print(f"✅ 已生成: {OUT}")
print(f"📏 总行数: {line_count}")
print(f"💾 文件大小: {OUT.stat().st_size/1024:.1f} KB")
