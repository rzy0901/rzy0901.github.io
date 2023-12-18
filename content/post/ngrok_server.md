---
title: "利用Ngrok实现内网穿透，并访问局域网下的openssh服务器"
date: 2023-12-18T20:29:44+08:00
lastmod: 2023-12-18T20:29:44+08:00
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
typora-copy-images-to: ../../static/Ngrok_server.assets
typora-root-url: ../../static
---

##  引子

事情的最初是实验室同门乾任和我，发现实验室一台没有人用的电脑具有两张3090显卡。我们问了一圈实验室，大家都忘记了密码，于是我们为这台电脑重新安装了linux系统以及[openssh](https://www.openssh.com/)等远程工具（安装过程很简单，略）。这使得我们得以在终端，vscode，mobaxterm等中便捷地远程访问服务器的环境（炼丹）。

简单来说，在校园网之下，我们只需要以下一行代码，便可以访问服务器：

```zsh
# ssh -p <port_number> <username>@<ip_address>
ssh -p 1220 lasso@10.16.20.194
```

运行示例：

![image-20231218204812386](/Ngrok_server.assets/image-20231218204812386.png)

然而，上述方法无法使得我们在非校园网的情况下访问服务器，主要原因是实验室服务器并没有一个公网ip地址。

## 内网穿透

我们可以使用免费内网穿透工具[Ngrok](https://dashboard.ngrok.com/)解决该问题。（安装过程很简单，略）

在内网或者使用向日葵登陆服务器，运行如下代码即可：

```zsh
# ngrok tcp <port_number>
# 该port_number默认为20，我们在/etc/ssh/sshd_config将端口号改为了1220
ngrok tcp 1220
```

接下来，我们有如下结果：

![ngrok](/Ngrok_server.assets/ngrok.PNG)

基于此，我们在公网下可通过如下代码访问课题组服务器：

 ```zsh
 # ssh -p <port_number> <username>@<ip_address>
 ssh -p 11808 lasso@0.tcp.ap.ngrok.io
 ```

> <p><font color="red" size="+2">需要注意的是：</font> 由于我们使用的是免费版 ngrok，每次运行 <code>ngrok tcp 1220</code> 所得到的公网 URL 以及端口号都是随机的。因此，每当服务器重新启动，我们需要更改上述代码。</p>


运行示例：

![image-20231218210144344](/Ngrok_server.assets/image-20231218210144344.png)
