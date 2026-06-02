---
title: "Frontmatter 结构化展示 vs 正文渲染 — 对比演示"
author: CodeBuddy
date: 2026-05-27
tags: [markdown, yaml, frontmatter, github]
description: "演示 GitHub 预览模式下 Frontmatter 被结构化展示、不混入正文的行为。"
draft: false
---

# Frontmatter 预览行为对比演示

本文件演示：**同一段 YAML Frontmatter，在不同工具/模式下的两种渲染结果**。

---

## 一、在 GitHub 预览中的样子（✅ 结构化展示）

打开本文件在 **GitHub.com** 上的 Preview 视图，你会看到顶部出现一个折叠面板：

```
┌─────────────────────────────────────────────────────────────┐
│                     📋 文件属性面板                          │
├──────────────┬──────────────────────────────────────────────┤
│  title       │  Frontmatter 结构化展示 vs 正文渲染 — 对比演示 │
│  author      │  CodeBuddy                                   │
│  date        │  2026-05-27                                  │
│  tags        │  markdown · yaml · frontmatter · github      │
│  description │  演示 GitHub 预览模式下…                      │
│  draft       │  false                                       │
└──────────────┴──────────────────────────────────────────────┘

↓ 正文从这里开始，Frontmatter 完全不出现在正文里 ↓
```

**关键特征：**
- `---` 不渲染为分隔线
- `title: "..."` 不显示为普通文字
- 元数据被单独解析、以表格/面板形式呈现
- 正文第一行直接是 `# 标题`，干净整洁

---

## 二、被"作为正文渲染"时的样子（❌ 错误行为）

如果解析器**不认识** Frontmatter，会把它当普通 Markdown 处理：

```
（渲染结果）

─────────────────────────   ← --- 被渲染成分隔线
title: "Frontmatter 结构化展示 vs 正文渲染 — 对比演示"
author: CodeBuddy
date: 2026-05-27
tags: [markdown, yaml, frontmatter, github]
description: "演示 GitHub 预览模式下…"
draft: false
─────────────────────────   ← 第二个 --- 也成了分隔线

# Frontmatter 预览行为对比演示

正文内容...
```

**问题：**
- 用户直接看到 `title: "..."` 这类配置文字
- `---` 变成两条多余的水平线
- 正文被配置信息"污染"，阅读体验差

---

## 三、各工具的实际表现

| 工具 | 预览行为 |
|:---|:---|
| **GitHub.com** | 折叠为可展开的属性面板（灰色背景），点击可查看原始 YAML |
| **VS Code**（内置预览） | 默认**不显示** Frontmatter，正文干净 |
| **Obsidian** | 顶部显示"Properties"结构化属性区，支持编辑 |
| **Typora** | 渲染为美观的信息表格，不混入正文 |
| **Hugo / Jekyll** | 构建时读取并注入模板变量，不输出到 HTML |
| **Hexo** | 同上，`title` 自动成为页面 `<title>` 标签 |
| **Pandoc** | 提取为文档元数据（作者、标题、日期），生成 PDF/Word 封面页 |
| **不支持的旧解析器** | ❌ 当普通文字渲染，出现"错误行为"中的乱码式输出 |

---

## 四、GitHub 的具体渲染规则

GitHub 对 Frontmatter 的支持遵循以下约定：

1. **触发条件**：文件以 `---\n` 开头（第一行必须是 `---`，前面无任何内容）
2. **结束标记**：遇到第二个 `---` 或 `...` 即结束 Frontmatter
3. **展示方式**：在文件预览顶部以**灰色折叠面板**展示，默认折叠
4. **不影响正文**：Frontmatter 区域被完整排除在正文渲染之外
5. **支持类型**：字符串、数字、布尔、列表、嵌套对象均可正确展示

### 示例：GitHub 面板截图示意

```
 ▼  title · author · date · tags · description · draft        ← 折叠/展开按钮

   title       Frontmatter 结构化展示 vs 正文渲染 — 对比演示
   author      CodeBuddy
   date        2026-05-27
   tags        markdown  yaml  frontmatter  github             ← 列表展示为标签
   description 演示 GitHub 预览模式下 Frontmatter 被结构化…
   draft       false
```

---

## 五、自己动手验证

将本文件上传到 GitHub 仓库，然后：

1. 点击文件名进入 **Preview 视图**
   → 看到顶部属性面板 ✅，正文从 `# Frontmatter 预览行为对比演示` 开始

2. 点击 **`<> Code`** 切回源码视图
   → 看到原始 `---` 包裹的 YAML ✅

3. 用一个**不支持 Frontmatter 的在线 Markdown 渲染器**（如早期版本的 Markdown Editor）粘贴本文件
   → 看到两条分隔线 + 键值对文字的"错误行为" ❌

---

> **总结一句话**：Frontmatter 是"给机器看的元数据"，GitHub 的预览模式把它结构化展示在独立面板里，让正文保持干净——这是约定俗成的正确行为，而非把 `title: xxx` 直接输出给读者。
