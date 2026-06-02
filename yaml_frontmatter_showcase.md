---
# ================================================================
# 示例 0：本文件自身的 Frontmatter（综合型）
# ================================================================
title: "YAML Frontmatter 全类型示例"
subtitle: "覆盖博客、文档、幻灯片、学术论文、Hugo、Jekyll、Hexo、Obsidian、Pandoc 等场景"
description: >
  本文件收录了在各种静态站点生成器、Markdown 工具链和知识管理软件中
  常见的 YAML Frontmatter 写法，涵盖字符串、数字、布尔、日期、列表、
  嵌套对象、多行文本、锚点与别名等所有 YAML 数据类型。
date: 2026-05-27
lastmod: 2026-05-27T20:10:00+08:00
author:
  name: "CodeBuddy"
  email: "codebuddy@example.com"
  url: "https://codebuddy.ai"
draft: false
toc: true
math: true
mermaid: true
---

# YAML Frontmatter 全类型示例

> 本文件演示在各种静态站点生成器（Hugo、Jekyll、Hexo、MkDocs）、写作工具（Obsidian、Typora）
> 和文档工具链（Pandoc、VuePress、Docusaurus）中常见的 **YAML Frontmatter** 写法，
> 涵盖全部 YAML 数据类型与真实场景模板。
[mermaid_showcase.md](mermaid_showcase.md)
---

## 目录

- [1. YAML 数据类型速览](#1-yaml-数据类型速览)
- [2. 博客文章（Jekyll / Hugo / Hexo）](#2-博客文章jekyll--hugo--hexo)
- [3. 文档页面（MkDocs / VuePress / Docusaurus）](#3-文档页面mkdocs--vuepress--docusaurus)
- [4. 幻灯片（Slidev / Marp / reveal.js）](#4-幻灯片slidev--marp--revealjs)
- [5. 学术论文（Pandoc / Quarto）](#5-学术论文pandoc--quarto)
- [6. 知识库笔记（Obsidian / Foam / Logseq）](#6-知识库笔记obsidian--foam--logseq)
- [7. 电子书章节（mdBook / GitBook）](#7-电子书章节mdbook--gitbook)
- [8. API 文档页面](#8-api-文档页面)
- [9. 产品更新日志](#9-产品更新日志)
- [10. 多语言国际化页面](#10-多语言国际化页面)
- [11. 电商商品页](#11-电商商品页)
- [12. 个人简历页](#12-个人简历页)
- [13. 开源项目 README](#13-开源项目-readme)
- [14. 数据分析报告](#14-数据分析报告)
- [15. YAML 高级语法演示](#15-yaml-高级语法演示)

---

## 1. YAML 数据类型速览

以下 Frontmatter 演示所有 YAML 原生数据类型：

```yaml
---
# ── 字符串 ──────────────────────────────────────────────────────
str_plain:    hello world
str_quoted:   "包含 :冒号 和 #井号 需加引号"
str_single:   '单引号：不解析 \n 转义'
str_double:   "双引号：解析 \n 换行 \t 制表"

# 多行字符串
str_literal: |
  字面块（literal block）：保留换行
  第二行
  第三行（末尾有一个换行）

str_folded: >
  折叠块（folded block）：换行变空格，
  适合长段落。段落间空行保留。

str_folded_strip: >-
  折叠+strip：去掉末尾所有换行符。

str_literal_keep: |+
  字面+keep：保留末尾所有换行符。


# ── 数字 ──────────────────────────────────────────────────────
int_decimal:    42
int_hex:        0x2A
int_octal:      0o52
int_binary:     0b101010
float_normal:   3.14159
float_sci:      6.022e23
float_inf:      .inf
float_neg_inf:  -.inf
float_nan:      .nan

# ── 布尔 ──────────────────────────────────────────────────────
bool_true_1:   true
bool_true_2:   True
bool_true_3:   yes          # YAML 1.1；YAML 1.2 中 yes 为字符串
bool_false_1:  false
bool_false_2:  False
bool_false_3:  no

# ── 空值 ──────────────────────────────────────────────────────
null_tilde:    ~
null_explicit: null
null_empty:

# ── 日期 & 时间 ──────────────────────────────────────────────
date_only:     2026-05-27
datetime_utc:  2026-05-27T12:00:00Z
datetime_tz:   2026-05-27T20:10:00+08:00
datetime_full: 2026-05-27 20:10:00.500 +0800

# ── 列表 ──────────────────────────────────────────────────────
list_block:
  - item A
  - item B
  - item C

list_flow:     [alpha, beta, gamma]

list_nested:
  - name: Alice
    role: admin
  - name: Bob
    role: editor

list_of_lists:
  - [1, 2, 3]
  - [4, 5, 6]

# ── 映射（对象）──────────────────────────────────────────────
map_block:
  host: localhost
  port: 5432
  ssl:  true

map_flow:      {x: 1, y: 2, z: 3}

map_nested:
  database:
    primary:
      host: db1.example.com
      port: 5432
    replica:
      host: db2.example.com
      port: 5432

# ── 锚点与别名 ────────────────────────────────────────────────
defaults: &defaults
  timeout: 30
  retries: 3
  loglevel: info

production:
  <<: *defaults         # 合并键（merge key）
  loglevel: warn

staging:
  <<: *defaults
  timeout: 60

# ── 多文档（--- 分隔，Frontmatter 通常只用一个）──────────────
---
```

---

## 2. 博客文章（Jekyll / Hugo / Hexo）

### 2.1 Jekyll 博客文章

```yaml
---
layout:     post
title:      "深入理解 Rust 所有权模型"
date:       2026-04-15 09:00:00 +0800
categories: [Rust, 系统编程]
tags:       [rust, ownership, borrow-checker, memory-safety]
author:     alice
permalink:  /rust/ownership/

# SEO
description: "全面解析 Rust 所有权、借用与生命周期，附大量代码示例。"
keywords:    "Rust, 所有权, 借用检查器"
image:       /assets/img/rust-ownership.png

# 特性开关
published:   true
comments:    true
toc:         true
pin:         false
math:        false

# 自定义变量（可在 Liquid 模板中用 {{ page.reading_time }} 访问）
reading_time: 12
difficulty:   intermediate
series:       Rust 系列
series_index: 3
---
```

### 2.2 Hugo 博客文章

```yaml
---
title:       "构建高性能 Go HTTP 服务"
description: "从零搭建支持 10 万 QPS 的 Go HTTP 服务，含压测与调优实录。"
date:        2026-03-20T10:30:00+08:00
lastmod:     2026-05-01T08:00:00+08:00
draft:       false
weight:      10

# 分类与标签
categories:  ["Go", "后端"]
tags:        ["go", "http", "performance", "benchmark"]
series:      ["Go 实战"]

# 作者（支持多作者）
authors:
  - name:   "Bob Chen"
    email:  "bob@example.com"
    github: "bobchen"

# 封面图
cover:
  image:   "/images/go-http.png"
  alt:     "Go HTTP Performance"
  caption: "Wrk 压测 Go HTTP Server"
  relative: false

# Hugo 特有
slug:        "high-performance-go-http"
aliases:     ["/posts/go-http-perf/", "/go/http/"]
url:         "/blog/go-http/"
canonicalURL: "https://example.com/blog/go-http/"

# 显示控制
showToc:        true
TocOpen:        false
ShowReadingTime: true
ShowWordCount:   true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowShareButtons: true
comments:       true
hidemeta:       false
searchHidden:   false

# Open Graph / Twitter Card
images: ["/images/go-http-og.png"]
---
```

### 2.3 Hexo 博客文章

```yaml
---
title:    Node.js 流式处理实战
date:     2026-02-10 14:20:00
updated:  2026-02-15 09:00:00
tags:
  - Node.js
  - Stream
  - 异步编程
categories:
  - 后端
  - Node.js
keywords: Node.js, Stream, Readable, Writable, Transform
description: 深入 Node.js Streams API，实现大文件高效处理。
cover: /images/nodejs-stream.png
thumbnail: /images/nodejs-stream-thumb.png
toc: true
comments: true

# Hexo 特有
excerpt: 本文通过实例讲解 Node.js Stream 的四种类型...
disableNunjucks: false
lang: zh-CN
---
```

---

## 3. 文档页面（MkDocs / VuePress / Docusaurus）

### 3.1 MkDocs Material 页面

```yaml
---
title:        快速开始
description:  五分钟上手教程，从安装到第一个 Hello World。
icon:         material/rocket-launch
status:       new            # new | deprecated

# 导航
hide:
  - navigation
  - toc
  - feedback

# 搜索
search:
  boost:   2
  exclude: false

# 标签
tags:
  - 入门
  - 教程
  - 安装

# 社交卡片
social_image: /assets/social/quickstart.png
---
```

### 3.2 VuePress 2 页面

```yaml
---
lang:         zh-CN
title:        配置参考
description:  完整的配置项说明文档。
head:
  - - meta
    - name:    keywords
      content: VuePress, 配置, 参考
  - - link
    - rel:  canonical
      href: https://example.com/config/

# 侧边栏 / 导航
sidebar:      auto
navbar:       true
prev:         ./installation.md
next:         ./plugins.md

# 页面元信息
editLink:         true
lastUpdated:      true
contributors:     true
pageClass:        custom-page-class
externalLinkIcon: false
---
```

### 3.3 Docusaurus 页面

```yaml
---
id:                configuration
title:             配置说明
sidebar_label:     配置
sidebar_position:  3
description:       所有可用配置项的完整参考。
keywords:
  - config
  - configuration
  - options
tags:
  - config
  - reference

# 显示控制
hide_title:         false
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 4
pagination_prev:    installation
pagination_next:    theming

# 自定义
custom_edit_url:    https://github.com/org/repo/edit/main/docs/config.md
draft:              false
unlisted:           false
---
```

---

## 4. 幻灯片（Slidev / Marp / reveal.js）

### 4.1 Slidev 演示文稿

```yaml
---
theme:      seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class:      text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition:  slide-left
title:       "微服务架构实践"
mdc:         true

# 自定义样式
fonts:
  sans:   Roboto
  serif:  Roboto Slab
  mono:   Fira Code

# 导出配置
exportFilename: microservices-slides
export:
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false
  withToc: false

# 信息面板
info: |
  ## 微服务架构实践
  讲师：Alice Wang
  日期：2026-05-27
---
```

### 4.2 Marp 幻灯片

```yaml
---
marp:          true
theme:         gaia
class:         lead
paginate:      true
header:        "微服务架构实践"
footer:        "© 2026 CodeBuddy"
backgroundColor: "#fff"
backgroundImage: url('https://example.com/bg.png')
size:          16:9
style: |
  section {
    font-family: 'PingFang SC', sans-serif;
  }
  h1 { color: #1a73e8; }
---
```

### 4.3 reveal.js（通过 Pandoc）

```yaml
---
title:    云原生安全实践
author:   Charlie Liu
date:     2026-05-27
theme:    moon
highlight-style: github
transition: fade
slideNumber: true
controls:   true
progress:   true
history:    true
center:     true
width:      1280
height:     720
margin:     0.04
minScale:   0.2
maxScale:   2.0
---
```

---

## 5. 学术论文（Pandoc / Quarto）

### 5.1 Pandoc 学术文章

```yaml
---
title:    "基于 Transformer 的多语言机器翻译综述"
subtitle: "2020–2025 年研究进展"
author:
  - name:        "张伟"
    affiliation: "清华大学计算机系"
    email:       "wei.zhang@tsinghua.edu.cn"
    orcid:       "0000-0001-2345-6789"
    corresponding: true
  - name:        "李娜"
    affiliation: "北京大学信息学院"
    email:       "na.li@pku.edu.cn"

date:     2026-05-27
abstract: |
  本文系统综述了 2020 年至 2025 年间基于 Transformer 架构的多语言机器翻译研究进展，
  重点分析了大规模预训练模型（mBERT、XLM-R、mT5）在低资源语言对上的表现，
  并对未来研究方向进行了展望。

keywords: [机器翻译, Transformer, 多语言, 预训练模型, 低资源]

# 引用
bibliography:  references.bib
csl:           chinese-gb7714-2015-numeric.csl
link-citations: true
nocite:        |
  @ref1, @ref2

# 格式输出
output:
  pdf_document:
    latex_engine: xelatex
    toc:          true
    toc_depth:    3
    number_sections: true
    citation_package: natbib
    keep_tex:     false
  html_document:
    theme:        flatly
    toc:          true
    toc_float:    true
    code_folding: show

# LaTeX 配置
documentclass:  article
papersize:      a4
fontsize:       12pt
geometry:       margin=2.5cm
linestretch:    1.5
indent:         true
numbersections: true
lang:           zh-CN
mainfont:       "Source Han Serif CN"
sansfont:       "Source Han Sans CN"
monofont:       "JetBrains Mono"
---
```

### 5.2 Quarto 文档

```yaml
---
title:        "数据可视化最佳实践"
author:       "Dana Park"
date:         last-modified
date-format:  "YYYY年MM月DD日"
lang:         zh

abstract: >
  本报告通过实例展示使用 ggplot2、Plotly 和 D3.js 进行
  数据可视化的最佳实践与常见误区。

# 格式
format:
  html:
    theme:         cosmo
    toc:           true
    toc-depth:     3
    toc-location:  left
    number-sections: true
    code-fold:     true
    code-tools:    true
    fig-width:     8
    fig-height:    5
    df-print:      paged
  pdf:
    toc:           true
    number-sections: true
    colorlinks:    true

# 执行选项
execute:
  echo:    true
  warning: false
  message: false
  cache:   true
  freeze:  auto

# 交叉引用
crossref:
  fig-title:    图
  tbl-title:    表
  fig-prefix:   图
  tbl-prefix:   表
  ref-hyperlink: true

# 书目
bibliography:  references.bib
citeproc:      true
---
```

---

## 6. 知识库笔记（Obsidian / Foam / Logseq）

### 6.1 Obsidian 笔记

```yaml
---
# 基本信息
id:        20260527201000
title:     "分布式系统——CAP 定理"
aliases:
  - CAP 定理
  - CAP Theorem
  - Consistency Availability Partition

# 时间
created:   2026-05-27T20:10:00
modified:  2026-05-27T20:10:00

# 分类
type:      concept            # concept | note | project | person | book | article
status:    evergreen          # seedling | budding | evergreen | archived
tags:
  - 分布式系统
  - 数据库
  - 理论基础
  - CAP

# 关联
links:
  - "[[BASE 定理]]"
  - "[[Raft 共识算法]]"
  - "[[Paxos 算法]]"
source:    "https://en.wikipedia.org/wiki/CAP_theorem"
author:    "Eric Brewer"
year:      2000

# 自定义
difficulty:  ⭐⭐⭐
importance:  ⭐⭐⭐⭐⭐
review_due:  2026-06-27
cssclasses: [wide-page, no-title]
---
```

### 6.2 Foam 笔记

```yaml
---
id:    cap-theorem
title: CAP 定理
tags:
  - distributed-systems
  - theory
date:  2026-05-27
type:  note
foam_template:
  name: concept
  filepath: concepts/$FOAM_TITLE.md
---
```

### 6.3 Logseq 页面属性（Frontmatter 风格）

```yaml
---
title:    CAP 定理学习笔记
tags:     [[分布式系统]], [[数据库理论]]
alias:    CAP, CAP Theorem
public:   true
created:  [[2026-05-27]]
source:   https://en.wikipedia.org/wiki/CAP_theorem
---
```

---

## 7. 电子书章节（mdBook / GitBook）

### 7.1 mdBook

```yaml
---
title:           第三章：所有权与借用
chapter_number:  3
part:            "核心概念"
description:     "深入理解 Rust 最独特的特性——所有权系统。"
keywords:
  - ownership
  - borrowing
  - lifetimes
draft:           false
---
```

### 7.2 GitBook

```yaml
---
title:       快速入门
description: 五分钟上手指南
category:    getting-started
order:       1
cover:       .gitbook/assets/quickstart.png
---
```

---

## 8. API 文档页面

```yaml
---
title:       用户认证接口
description: OAuth 2.0 / JWT 认证接口完整文档
version:     v2.3.0
status:      stable          # stable | beta | deprecated | experimental
deprecated:  false
since:       v1.0.0

# API 元信息
api:
  base_url:   https://api.example.com/v2
  method:     POST
  path:       /auth/token
  auth:
    type:     oauth2
    flow:     client_credentials
    scopes:   [read, write, admin]

# 请求/响应
request:
  content_type: application/json
  rate_limit:
    requests: 1000
    window:   60s

# 分类
tags:         [认证, OAuth, JWT, 安全]
category:     Authentication
group:        Core APIs

# 生成工具
openapi:      ./openapi.yaml
operationId:  createToken
externalDocs:
  description: OAuth 2.0 规范
  url:         https://oauth.net/2/
---
```

---

## 9. 产品更新日志

```yaml
---
title:        v2.5.0 发布说明
version:      2.5.0
release_date: 2026-05-27
type:         minor            # major | minor | patch | hotfix
status:       released         # draft | released | yanked

# 变更分类
changes:
  breaking: false
  features:
    - 新增深色模式支持
    - 引入插件 API v2
    - 支持 YAML Frontmatter 嵌套锚点
  improvements:
    - 渲染速度提升 40%
    - 内存占用降低 25%
    - 错误信息更加友好
  bug_fixes:
    - 修复 Mermaid 图在 Safari 下渲染异常
    - 修复多语言环境下日期格式不正确
    - 修复大文件（>10MB）编辑卡顿问题
  security:
    - 升级 marked.js 至 12.0.0 修复 XSS 漏洞（CVE-2026-12345）
  deprecated:
    - 旧版插件 API v1 将在 v3.0.0 中移除

# 贡献者
contributors:
  - alice
  - bob
  - charlie
milestone: https://github.com/org/repo/milestone/25
compare:   https://github.com/org/repo/compare/v2.4.0...v2.5.0
---
```

---

## 10. 多语言国际化页面

```yaml
---
# 当前语言版本
title:    "Privacy Policy"
lang:     en
ref:      privacy-policy      # 跨语言关联 key

# 其他语言版本
translations:
  zh-CN:
    title: 隐私政策
    url:   /zh-CN/privacy/
  ja:
    title: プライバシーポリシー
    url:   /ja/privacy/
  ko:
    title: 개인정보 처리방침
    url:   /ko/privacy/
  fr:
    title: Politique de confidentialité
    url:   /fr/privacy/
  de:
    title: Datenschutzrichtlinie
    url:   /de/privacy/
  es:
    title: Política de privacidad
    url:   /es/privacy/

# hreflang 提示
hreflang:
  x-default: /en/privacy/

# 最后翻译更新
translated_at: 2026-05-27
translator:    i18n-team
---
```

---

## 11. 电商商品页

```yaml
---
title:          "MacBook Pro 16 英寸（2026）"
description:    "搭载 M5 Pro 芯片，专为专业创作者打造。"
type:           product
sku:            MBP-16-M5PRO-512

# 商品信息
product:
  brand:        Apple
  model:        MacBook Pro 16
  year:         2026
  chip:         M5 Pro
  memory:       [16, 32, 48, 64]    # GB 可选
  storage:      [512, 1024, 2048]   # GB 可选
  colors:
    - name: 深空黑色
      hex:  "#1d1d1f"
    - name: 银色
      hex:  "#f5f5f0"
  dimensions:
    width:   35.57   # cm
    depth:   24.81
    height:  1.68
    weight:  2.14    # kg

# 价格
pricing:
  currency:     CNY
  base_price:   19999
  sale_price:   18999
  on_sale:      true
  sale_ends:    2026-06-18T23:59:59+08:00

# SEO & 电商
images:
  - src: /images/mbp-front.jpg
    alt: MacBook Pro 正面
  - src: /images/mbp-side.jpg
    alt: MacBook Pro 侧面

schema_org:
  type:          Product
  availability:  InStock
  rating:
    value:  4.9
    count:  2840
---
```

---

## 12. 个人简历页

```yaml
---
title:    "张伟 — 全栈工程师"
layout:   resume
lang:     zh-CN

# 个人信息
personal:
  name:       张伟
  name_en:    Wei Zhang
  title:      高级全栈工程师
  location:   北京，中国
  email:      wei@example.com
  phone:      "+86-138-0000-0000"
  website:    https://weizhang.dev
  github:     github.com/weizhang
  linkedin:   linkedin.com/in/weizhang
  avatar:     /images/avatar.jpg
  summary: >
    8 年全栈开发经验，专注云原生架构与高性能系统设计，
    主导过日均千万级流量系统的设计与落地。

# 技能
skills:
  languages:   [Go, TypeScript, Python, Rust, SQL]
  frameworks:  [React, Next.js, Gin, FastAPI, gRPC]
  databases:   [PostgreSQL, MySQL, Redis, MongoDB, ClickHouse]
  devops:      [Kubernetes, Docker, Terraform, GitHub Actions, Prometheus]
  tools:       [Git, Figma, Postman, Jira]

# 工作经历
experience:
  - company:    字节跳动
    title:      技术专家
    start:      2022-07
    end:        present
    location:   北京
    highlights:
      - 主导广告投放系统重构，P99 延迟从 120ms 降至 18ms
      - 设计并落地微服务拆分方案，服务数量从 15 增至 60+
  - company:    阿里巴巴
    title:      高级工程师
    start:      2019-06
    end:        2022-06
    location:   杭州

# 教育
education:
  - school:    清华大学
    degree:    硕士
    major:     计算机科学
    start:     2015
    end:       2018
  - school:    北京大学
    degree:    学士
    major:     软件工程
    start:     2011
    end:       2015

# 证书
certifications:
  - name: CKA (Certified Kubernetes Administrator)
    issuer: CNCF
    date: 2024-03
  - name: AWS Solutions Architect Professional
    issuer: Amazon
    date: 2023-11
---
```

---

## 13. 开源项目 README

```yaml
---
title:        "FastCache"
description:  "一个用 Go 编写的高性能内存缓存库，零依赖，API 简洁。"
version:      "1.4.2"
license:      "MIT"
homepage:     "https://github.com/example/fastcache"

# 徽章配置（用于模板渲染）
badges:
  build:   "https://github.com/example/fastcache/actions/workflows/ci.yml/badge.svg"
  coverage:"https://codecov.io/gh/example/fastcache/branch/main/graph/badge.svg"
  godoc:   "https://pkg.go.dev/badge/github.com/example/fastcache"
  goreport:"https://goreportcard.com/badge/github.com/example/fastcache"
  version: "https://img.shields.io/github/v/release/example/fastcache"

# 项目元信息
project:
  language:     Go
  go_version:   ">=1.22"
  os:           [linux, macOS, windows]
  arch:         [amd64, arm64]
  stars:        3840
  forks:        214
  open_issues:  12

# 维护者
maintainers:
  - name:   Alice Wang
    github: alicewang
    role:   lead
  - name:   Bob Chen
    github: bobchen
    role:   contributor

# 快速链接
links:
  docs:       "https://fastcache.example.com"
  changelog:  "CHANGELOG.md"
  contributing: "CONTRIBUTING.md"
  roadmap:    "https://github.com/example/fastcache/projects/1"
---
```

---

## 14. 数据分析报告

```yaml
---
title:        "2026 Q1 用户增长分析报告"
subtitle:     "核心指标解读与策略建议"
type:         report
classification: internal       # public | internal | confidential
version:      1.2

# 报告信息
report:
  period:
    start: 2026-01-01
    end:   2026-03-31
  published:   2026-04-15
  reviewed_by: [产品总监, 数据分析团队]
  approved_by: VP of Product

# 关键指标快照
kpis:
  dau:
    value:  2580000
    growth: +12.4%
    mom:    +3.1%
  mau:
    value:  18400000
    growth: +8.7%
  retention_d7:   42.3%
  retention_d30:  21.8%
  conversion:
    free_to_paid:  3.2%
    mom_change:    +0.4pp

# 数据来源
data_sources:
  - name:    ClickHouse 数仓
    version: "2026-04-01"
    tables:  [user_events, user_profiles, orders]
  - name:    GA4
    account: UA-XXXXXXX

# 可视化工具
charts:
  library:  Plotly
  theme:    light
  export:   [png, svg]

# 依赖
requires:
  python:    ">=3.11"
  packages:  [pandas, plotly, scipy, statsmodels]
---
```

---

## 15. YAML 高级语法演示

```yaml
---
# ── 锚点（&）与别名（*）────────────────────────────────────────
default_server: &srv_base
  protocol: https
  timeout:  30
  retries:  3
  headers:
    Accept:       application/json
    Content-Type: application/json

production_api:
  <<: *srv_base           # 合并 default_server 的所有键
  host: api.example.com
  port: 443

staging_api:
  <<: *srv_base
  host: staging-api.example.com
  port: 8443
  timeout: 60             # 覆盖合并来的 timeout

# ── 显式类型标签（!!）──────────────────────────────────────────
explicit_types:
  integer:    !!int    "42"
  float:      !!float  "3.14"
  bool:       !!bool   "true"
  string:     !!str    42          # 数字强转为字符串
  binary:     !!binary |
    R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
  timestamp:  !!timestamp 2026-05-27T20:10:00+08:00

# ── 复杂嵌套与循环引用（文档说明，实际不推荐）──────────────────
matrix:
  - &row1 [1, 2, 3]
  - &row2 [4, 5, 6]
  - &row3 [7, 8, 9]

matrix_ref:
  first_row:  *row1
  second_row: *row2
  third_row:  *row3

# ── 多行字符串的各种写法 ───────────────────────────────────────
multiline:
  # | 字面块：原样保留换行，末尾保留一个 \n
  literal: |
    line one
    line two
    line three

  # > 折叠块：换行变空格，空行变换行
  folded: >
    This is a very long sentence that
    will be folded into a single line.

    This is a new paragraph.

  # |- strip：去掉末尾所有换行
  strip: |-
    no trailing newline

  # |+ keep：保留末尾所有换行
  keep: |+
    preserve trailing newlines


  # 缩进指示符：明确指定缩进量
  indent2: |2
    indented by 2
    still indented by 2

# ── 流式（行内）vs 块式 ────────────────────────────────────────
block_sequence:
  - item1
  - item2
  - item3

flow_sequence:  [item1, item2, item3]

block_mapping:
  key1: val1
  key2: val2

flow_mapping:   {key1: val1, key2: val2}

# ── 嵌套流式 ────────────────────────────────────────────────────
matrix_flow: [[1,2,3],[4,5,6],[7,8,9]]

users_flow:
  - {name: Alice, role: admin,  active: true}
  - {name: Bob,   role: editor, active: false}
  - {name: Carol, role: viewer, active: true}

# ── 特殊键名（含特殊字符需引号）──────────────────────────────
special_keys:
  "key:with:colons":   value1
  "key with spaces":   value2
  "key#with#hash":     value3
  123:                 numeric-key
  true:                bool-key-as-string
  "":                  empty-key

# ── 不同引号规则 ───────────────────────────────────────────────
quotes:
  no_quotes:    simple string
  double:       "解析 \n \t \u0041 等转义"
  single:       '不解析 \n，字面量 \t'
  double_colon: "value: with colon"
  url:          "https://example.com/path?q=1&r=2"
  json_like:    '{"key": "value"}'

# ── 数值边界 ────────────────────────────────────────────────────
numbers:
  max_int:      9223372036854775807
  min_int:      -9223372036854775808
  small_float:  1.7976931348623157e+308
  hex:          0xFF
  octal:        0o77
  inf:          .inf
  neg_inf:      -.inf
  not_a_number: .nan

# ── 日期时间全格式 ─────────────────────────────────────────────
dates:
  date:          2026-05-27
  datetime_z:    2026-05-27T20:10:00Z
  datetime_tz:   2026-05-27T20:10:00+08:00
  datetime_ms:   2026-05-27T20:10:00.123Z
  datetime_us:   2026-05-27T20:10:00.123456Z
  canonical:     2026-05-27 20:10:00.5 +0800
---
```

---

## 附录：各工具 Frontmatter 字段速查

| 字段 | Jekyll | Hugo | Hexo | Obsidian | Pandoc | Quarto |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| `title` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `date` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `draft` | ✅ | ✅ | ✅ | — | — | ✅ |
| `tags` | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| `categories` | ✅ | ✅ | ✅ | — | — | — |
| `layout` | ✅ | — | ✅ | — | — | — |
| `weight` | — | ✅ | — | — | — | — |
| `lastmod` | — | ✅ | `updated` | `modified` | — | — |
| `aliases` | — | ✅ | — | ✅ | — | — |
| `cover` | — | ✅ | ✅ | — | — | — |
| `math` | — | ✅ | — | — | `--mathjax` | `math: true` |
| `toc` | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| `author` | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| `bibliography` | — | — | — | — | ✅ | ✅ |
| `output` | — | — | — | — | ✅ | ✅ |
| `lang` | — | ✅ | — | — | ✅ | ✅ |

---

*文件生成时间：2026-05-27 | 覆盖工具：Jekyll、Hugo、Hexo、MkDocs、VuePress、Docusaurus、Slidev、Marp、reveal.js、Pandoc、Quarto、Obsidian、Foam、Logseq、mdBook、GitBook*
