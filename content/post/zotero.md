---
title: "利用Icloud对Zotero参考文献进行多端同步（MAC，Windows）"
date: 2025-04-12T14:26:59+08:00
lastmod: 2025-04-12T14:26:59+08:00
draft: false
keywords: []
description: ""
tags: []
categories: []
author: "Ren Zhenyu"

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: true
toc: true
autoCollapseToc: true
postMetaInFooter: true
hiddenFromHomePage: false
# You can also define another contentCopyright. e.g. contentCopyright: "This is another copyright."
contentCopyright: MIT
reward: false
mathjax: true
mathjaxEnableSingleDollar: true
mathjaxEnableAutoNumber: true

# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false

# You can enable or disable out-of-date content warning for individual post.
# Comment this out to use the global config.
#enableOutdatedInfoWarning: false

flowchartDiagrams:
  enable: true
  options: ""

sequenceDiagrams: 
  enable: true
  options: ""
# typora-copy-images-to: ../../static/Zotero.assets
typora-copy-images-to: ../../static/zotero.assets
typora-root-url: ../../static
---

<!--more-->

> + 最近新购买了一台笔记本流程，发现要把曾经的Zotero文献同步机制再走一遍，特此简要记录了一下需要的指令。
> + 大体思路就是利用zotero官方的同步来记录文献的条目（索引），而文献的pdf storage则使用icloud来记录，需要使用软连接指令将icloud云盘的文件夹链接到zotero指定的路径之下。

参考连接：
+ <https://zhuanlan.zhihu.com/p/608834534>
+ <https://notarocketscientist.xyz/posts/2022-10-04-using-zotero-with-icloud-as-the-storage/>（这个连接靠谱一点，第一个废话连篇）


## MAC指令
```
ln -s <source_directory_fullFilePath> <target_directory_parentDirPath>
```

```
ln -s /Users/renzhenyu/Library/Mobile\ Documents/com\~apple\~CloudDocs/Zotero/storage /Users/renzhenyu/Zotero/
```

## Windows指令
```
mklink /D "<target_directory_fullFilePath>" "<source_directory_fullFilePath>"
```

```
mklink /D "C:\Users\admin\Zotero\storage" "C:\Users\admin\iCloudDrive\Zotero\storage"
```

