# WorkBuddy/CodeBuddy Chat 抓包配置指南

> 用 whistle 抓取 completions 和 /v2/report 等 HTTPS 请求

---

## 成功配置总结（macOS）

### 生效的关键配置（缺一不可）

| # | 配置项 | 作用 | 位置 |
|---|--------|------|------|
| 1 | `settings.json` 代理配置 | 让 WorkBuddy 部分网络层走代理 | `~/Library/Application Support/WorkBuddy/User/settings.json` |
| 2 | `launchctl setenv` 环境变量 | 让 Node.js 进程读到 `HTTPS_PROXY` | macOS 全局环境变量 |
| 3 | whistle HTTPS 拦截开启 | 解密 HTTPS 流量看到请求内容 | whistle Web UI 或 API |
| 4 | whistle 规则 `disable://verify-peer` | 绕过 SSL Pinning | whistle 规则配置 |
| 5 | `NODE_TLS_REJECT_UNAUTHORIZED=0` | Node.js 接受 whistle 自签名证书 | 环境变量 |

### 第一步：安装并启动 whistle

```bash
# 安装
brew install whistle
# 或
npm install -g whistle

# 启动（默认端口 8899）
w2 start
```

### 第二步：settings.json 代理配置

编辑 `~/Library/Application Support/WorkBuddy/User/settings.json`，添加：

```json
{
    "http.proxy": "http://127.0.0.1:8899",
    "http.proxyStrictSSL": false,
    "codingcopilot.httpProxySettings": "override",
    "codingcopilot.httpProxy": "http://127.0.0.1:8899"
}
```

### 第三步：设置环境变量（关键！）

```bash
launchctl setenv HTTP_PROXY http://127.0.0.1:8899
launchctl setenv HTTPS_PROXY http://127.0.0.1:8899
launchctl setenv http_proxy http://127.0.0.1:8899
launchctl setenv https_proxy http://127.0.0.1:8899
launchctl setenv NODE_TLS_REJECT_UNAUTHORIZED 0
```

> **为什么需要环境变量？** WorkBuddy Chat 的 completions 请求由 Electron 主进程内的 Node.js 发出，它不读 `settings.json` 的 `http.proxy`，只认环境变量 `HTTPS_PROXY`。

### 第四步：whistle 开启 HTTPS 拦截

方法一：打开 whistle Web UI（`http://127.0.0.1:8899`），点击顶部 HTTPS 按钮，勾选拦截

方法二：API 方式
```bash
curl -X POST http://127.0.0.1:8899/cgi-bin/intercept-https-connects \
  -d 'clientId=cli&interceptHttpsConnects=1'
```

### 第五步：添加 whistle 规则

在 whistle Web UI 的 Rules 中添加：
```
copilot.tencent.com disable://verify-peer
```

### 第六步：重启 WorkBuddy

```bash
# ⌘Q 完全退出 WorkBuddy，然后重新打开
# 或从终端启动确保继承环境变量：
HTTPS_PROXY=http://127.0.0.1:8899 \
HTTP_PROXY=http://127.0.0.1:8899 \
NODE_TLS_REJECT_UNAUTHORIZED=0 \
/Applications/WorkBuddy.app/Contents/MacOS/Electron
```

### 验证

```bash
# 检查是否有连接到 whistle
lsof -i :8899 -P -n | grep -i "Electron\|WorkBuddy"

# 在 whistle Web UI 中查看抓到的请求
# 搜索 copilot.tencent.com
```

### 清理（不需要抓包时）

```bash
# 移除环境变量
launchctl setenv HTTP_PROXY ""
launchctl setenv HTTPS_PROXY ""
launchctl setenv NODE_TLS_REJECT_UNAUTHORIZED ""

# 停止 whistle
w2 stop

# 移除 settings.json 中的代理配置（可选）
```

---

## Windows 配置指南

### 前提

- 安装 Node.js
- 安装 whistle：`npm install -g whistle`

### 第一步：启动 whistle

```cmd
w2 start
```

whistle 默认监听 `127.0.0.1:8899`，Web UI 地址：`http://127.0.0.1:8899`

### 第二步：settings.json 代理配置

编辑 WorkBuddy 的 settings.json：

```
%APPDATA%\WorkBuddy\User\settings.json
```

> 如果是 CodeBuddy CN：`%APPDATA%\CodeBuddy CN\User\settings.json`

添加以下配置：

```json
{
    "http.proxy": "http://127.0.0.1:8899",
    "http.proxyStrictSSL": false,
    "codingcopilot.httpProxySettings": "override",
    "codingcopilot.httpProxy": "http://127.0.0.1:8899"
}
```

### 第三步：设置系统环境变量（关键！）

#### 方法一：临时设置（仅当前终端会话）

```cmd
set HTTP_PROXY=http://127.0.0.1:8899
set HTTPS_PROXY=http://127.0.0.1:8899
set NODE_TLS_REJECT_UNAUTHORIZED=0
```

PowerShell：
```powershell
$env:HTTP_PROXY = "http://127.0.0.1:8899"
$env:HTTPS_PROXY = "http://127.0.0.1:8899"
$env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
```

#### 方法二：永久设置（推荐，所有新进程生效）

```cmd
setx HTTP_PROXY http://127.0.0.1:8899
setx HTTPS_PROXY http://127.0.0.1:8899
setx http_proxy http://127.0.0.1:8899
setx https_proxy http://127.0.0.1:8899
setx NODE_TLS_REJECT_UNAUTHORIZED 0
```

> **注意**：`setx` 设置的变量对**已打开**的窗口不生效，需要打开新的 cmd/PowerShell 或重启应用。

#### 方法三：通过 GUI 设置

1. Win + R → `sysdm.cpl` → 高级 → 环境变量
2. 在"用户变量"中新建：
   - `HTTP_PROXY` = `http://127.0.0.1:8899`
   - `HTTPS_PROXY` = `http://127.0.0.1:8899`
   - `NODE_TLS_REJECT_UNAUTHORIZED` = `0`

### 第四步：whistle 开启 HTTPS 拦截

打开 `http://127.0.0.1:8899`，点击顶部 **HTTPS** 按钮：
1. 勾选 **Intercept HTTPS CONNECTs**
2. 点击 **Download RootCA** 下载证书
3. 双击证书安装到 **受信任的根证书颁发机构**

或 API 方式：
```cmd
curl -X POST http://127.0.0.1:8899/cgi-bin/intercept-https-connects -d "clientId=cli&interceptHttpsConnects=1"
```

### 第五步：添加 whistle 规则

在 whistle Web UI → Rules 中添加规则：
```
copilot.tencent.com disable://verify-peer
```

### 第六步：重启 WorkBuddy

完全关闭 WorkBuddy（托盘图标右键退出），然后：

#### 方法一：从设置了环境变量的终端启动

```cmd
# 先设置环境变量（如果用的临时方式）
set HTTPS_PROXY=http://127.0.0.1:8899
set HTTP_PROXY=http://127.0.0.1:8899
set NODE_TLS_REJECT_UNAUTHORIZED=0

# 启动 WorkBuddy
start "" "C:\Users\你的用户名\AppData\Local\Programs\WorkBuddy\WorkBuddy.exe"
```

PowerShell：
```powershell
$env:HTTPS_PROXY = "http://127.0.0.1:8899"
$env:HTTP_PROXY = "http://127.0.0.1:8899"
$env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
& "C:\Users\你的用户名\AppData\Local\Programs\WorkBuddy\WorkBuddy.exe"
```

#### 方法二：如果用了 setx 永久设置，直接双击图标启动即可

> `setx` 的优势就是不需要从终端启动，任何方式启动的新进程都会拿到变量。

### 验证

```cmd
# 检查 whistle 是否在运行
netstat -an | findstr 8899

# 在 whistle Web UI 中查看抓到的请求
# 搜索 copilot.tencent.com
```

### 清理（不需要抓包时）

```cmd
# 删除环境变量
setx HTTP_PROXY ""
setx HTTPS_PROXY ""
setx NODE_TLS_REJECT_UNAUTHORIZED ""

# 或在 GUI 中删除对应变量

# 停止 whistle
w2 stop
```

---

## 踩坑记录

| 坑 | 说明 |
|----|------|
| `settings.json` 的 `http.proxy` 对 completions 请求无效 | Chat 的 completions 请求由 Electron 主进程的 Node.js 发出，不走 VSCode 的 network service |
| macOS Wi-Fi 代理设置无效 | Node.js 不读系统代理配置 |
| `launchctl setenv` 可能不被 GUI 应用继承 | 依赖启动方式，从终端启动最可靠 |
| whistle HTTPS 拦截默认关闭 | 不开的话只能看到 CONNECT 隧道，看不到请求内容 |
| 需要 `NODE_TLS_REJECT_UNAUTHORIZED=0` | 否则 Node.js 会拒绝 whistle 的自签名证书 |
| 需要 `disable://verify-peer` 规则 | 绕过 copilot.tencent.com 的 SSL Pinning |

---

## 快速一键脚本

### macOS

```bash
#!/bin/bash
# whistle-workbuddy-proxy.sh - 一键开启 WorkBuddy 抓包

# 启动 whistle
w2 start

# 开启 HTTPS 拦截
curl -s -X POST http://127.0.0.1:8899/cgi-bin/intercept-https-connects \
  -d 'clientId=cli&interceptHttpsConnects=1'

# 设置环境变量
launchctl setenv HTTP_PROXY http://127.0.0.1:8899
launchctl setenv HTTPS_PROXY http://127.0.0.1:8899
launchctl setenv NODE_TLS_REJECT_UNAUTHORIZED 0

echo "✅ 代理已配置，请 ⌘Q 重启 WorkBuddy"
```

### Windows

```bat
@echo off
REM whistle-workbuddy-proxy.bat - 一键开启 WorkBuddy 抓包

REM 启动 whistle
start /b w2 start

REM 等待 whistle 启动
timeout /t 3 /nobreak >nul

REM 开启 HTTPS 拦截
curl -s -X POST http://127.0.0.1:8899/cgi-bin/intercept-https-connects -d "clientId=cli&interceptHttpsConnects=1"

REM 设置永久环境变量
setx HTTP_PROXY http://127.0.0.1:8899
setx HTTPS_PROXY http://127.0.0.1:8899
setx NODE_TLS_REJECT_UNAUTHORIZED 0

echo.
echo ✅ 代理已配置，请完全退出并重启 WorkBuddy
pause
```
