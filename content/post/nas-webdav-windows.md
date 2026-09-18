---
title: "把 NAS 挂到 Windows：一次 HTTPS WebDAV 实践记录"
date: 2026-09-18T00:00:00+08:00
lastmod: 2026-09-18T00:00:00+08:00
draft: false
description: "使用 rclone 和 WinFsp 访问已授权 NAS，区分网页入口与文件服务，并验证外网连接。"
tags: ["NAS", "WebDAV", "Windows", "部署记录", "AI生成"]
categories: ["技术实践"]
author: "Ren Zhenyu / AI 辅助生成"
toc: true
autoCollapseToc: false
reward: false
mathjax: false
---

> **AI 生成标识：** 本文由 AI 根据一次实际操作记录整理生成。命令与地址已脱敏；已验证结果与尚未完成的配置分别说明。

这次需求很简单：把自己获授权使用的 NAS 挂成 Windows 盘符，既能在资源管理器里浏览，也能让分析程序直接读取文件。最终通过 HTTPS WebDAV 完成只读挂载，并切换到手机热点验证了外网访问。

<!--more-->

## 网页能打开，不等于能挂载

NAS 的管理网页、FTP、WebDAV 是不同的入口。能登录管理界面，只能证明网页服务可达，并不表示 WebDAV 已启用或开放给当前网络。

资源管理器中的 FTP“网络位置”也不等于普通盘符。需要让命令行和分析程序读取文件时，可以使用 **rclone + WinFsp** 提供文件系统挂载。

## 准备与配置

先由管理员启用 HTTPS WebDAV，确认账号权限、访问地址和证书。Synology 的 HTTPS WebDAV 常用端口是 **5006**，实际端口以服务器配置为准；外部访问还需要网络侧允许该服务。

Windows 安装 [WinFsp](https://winfsp.dev/) 和 [rclone](https://rclone.org/install/)。便携版 rclone 可放在 `%LOCALAPPDATA%\Programs\rclone\`，将该目录加入用户 PATH，重新打开终端后检查：

```powershell
rclone version
rclone config
```

在交互配置中创建名为 `nas_webdav` 的 remote：

| 项目 | 示例设置 |
| --- | --- |
| Storage | `webdav` |
| URL | `https://nas.example.com:5006/` |
| Vendor | `other` |
| User / Password | 在本机交互输入自己的授权账号密码 |

`nas.example.com` 是占位域名，不能直接使用。不要把密码写进命令、博客或 Git；rclone 默认配置里的密码只是混淆存储，并非安全保险箱，配置文件也应按凭据保护。

## 先验证，再挂载

先直接请求服务器列出根目录：

```powershell
rclone lsd "nas_webdav:/" --contimeout 10s --timeout 20s --retries 1
```

确认成功且 `S:` 空闲后，挂载账号可访问的全部共享目录：

```powershell
rclone mount "nas_webdav:/" S: --read-only --vfs-cache-mode full --vfs-cache-max-size 2G
```

然后在资源管理器打开 `S:\`。这里的“全部”仍受账号权限约束，不会获得额外权限。`--read-only` 适合查看和分析，避免误改原始文件；缓存上限是管理目标，正在使用的文件等情况可能使缓存暂时超出限制。

前台运行时需保持终端开启，按 `Ctrl+C` 卸载。若要登录后自动挂载，可在证书和连接验证完成后使用 Windows 任务计划程序，以需要访问盘符的用户身份启动，并记录运行日志。

## 外网验证不要只看缓存

我切换到手机热点后，重新运行了 `rclone lsd`，并通过 `rclone cat` 直接读取服务器上的一份已知文件。两个请求都成功，才确认当时的外网连接可用。

```powershell
rclone cat "nas_webdav:/Shared/example.txt" --head 256 --contimeout 10s --timeout 20s
```

示例文件路径需要替换。仅在资源管理器里打开已经读过的文件不够，因为挂载缓存可能让断网后的文件仍然可见；直接调用 remote 的这些命令不会使用挂载盘的 VFS 缓存。

## 这次遇到的三个问题

| 现象 | 排查方向 |
| --- | --- |
| 连接超时或被拒绝 | 服务是否启动、端口是否开放、DNS 和应用网络路径是否正确 |
| `401 Unauthorized` | 已收到 HTTP 服务响应，但认证尚未通过；再核对账号、密码与权限 |
| 证书验证失败 | 证书是否受信任、是否过期，以及名称是否匹配访问域名 |

域名还可能经过反向代理或 CDN。以 Cloudflare 标准代理为例，其支持的 HTTPS 端口列表不包含 5006，因此不能简单在已有管理域名后加上 `:5006`。应由管理员提供正确的 WebDAV 入口，例如受控直连地址，或通过 HTTPS 443 反向代理文件服务。

本次实际验证遇到了 NAS 默认证书名称不匹配的问题，临时诊断与挂载跳过了证书校验。因此，**已验证的是文件服务连通与读取成功，不是证书配置已经合格**。跳过校验虽然仍有加密，却失去可靠的服务器身份验证，不作为本文的长期配置示例；正式自动挂载前，应由管理员配置匹配域名的有效证书，或按组织要求建立受控证书信任。

本文仅记录授权存储访问和文件管理经验，不涉及未授权访问或绕过访问控制。实际部署遵守所在地法律法规及单位网络、数据管理要求。

## 以后记录部署经验的一句 Prompt

> 请把本次已经验证的部署经验整理成一篇简短博客，写入我的博客项目并标注 AI 生成，使用示例地址替换真实主机、账号和私有路径，排除密码、令牌及敏感数据，不包含未授权访问或违法用途的操作内容，明确已验证结果与未完成事项，完成构建和隐私检查后按本次授权的部署方式发布，并返回文章链接与验证结果。

## 参考资料

- [rclone WebDAV 配置](https://rclone.org/webdav/)
- [rclone mount：Windows 挂载与缓存说明](https://rclone.org/commands/rclone_mount/)
- [rclone 安装及自动启动](https://rclone.org/install/)
- [Cloudflare 标准代理支持的网络端口](https://developers.cloudflare.com/fundamentals/reference/network-ports/)
