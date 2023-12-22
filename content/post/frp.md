---
title: "基于Frp的内网穿透，校园网外ssh访问实验室服务器"
date: 2023-12-22T21:16:05+08:00
lastmod: 2023-12-22T21:16:05+08:00
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
typora-copy-images-to: ../../static/Frp.assets
typora-root-url: ../../static
---

<!--more-->

Reference: [Access your computer in a LAN network via SSH](https://github.com/fatedier/frp?tab=readme-ov-file#access-your-computer-in-a-lan-network-via-ssh).

## **On server A (in the LAN):**

+ set up  `frp` client:

  ```zsh
  wget https://github.com/fatedier/frp/releases/download/v0.53.2/frp_0.53.2_linux_amd64.tar.gz
  tar -zxvf frp_0.53.2_linux_amd64.tar.gz
  cd frp_0.53.2_linux_amd64
  nano frpc.toml
  ```

  ```toml
  # frpc.toml
  serverAddr = "43.139.224.203" # public IP
  serverPort = 7000
  
  [[proxies]]
  name = "ssh"
  type = "tcp"
  localIP = "127.0.0.1"
  localPort = 1220
  remotePort = 6000
  ```

  + Make `6000` and `7000` accessible: `sudo ufw allow 6000` and`sudo ufw allow 7000` .

+ run `frp` client by

  ```zsh
  ./frpc -c ./frpc.toml
  ```

  or

  ```zsh
  nohup ./frpc -c ./frpc.toml &
  ```
  If any conflicts:
  
  ```zsh
  pkill -f frpc

## **On server B (with a public ip address):**

+ set up  `frp` server:

  ```zsh
  wget https://github.com/fatedier/frp/releases/download/v0.53.2/frp_0.53.2_linux_amd64.tar.gz
  tar -zxvf frp_0.53.2_linux_amd64.tar.gz
  cd frp_0.53.2_linux_amd64
  nano frps.toml
  ```

  ```toml
  # frps.toml
  bindPort = 7000
  ```

+ run `frp` server by

  ```zsh
  ./frps -c ./frps.toml
  ```

  or

  ```zsh
  nohup ./frps -c ./frps.toml &
  ```
  
  if any coflicts:
  
  ```zsh
  pkill -f frps
  ```

## **On your computer oustide the LAN containing server B:**

```zsh
ssh -oPort=6000 lasso@43.139.224.203
```
