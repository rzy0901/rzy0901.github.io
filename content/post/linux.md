---
title: "Linux Summary"
date: 2022-05-12T00:00:00+08:00
lastmod: 2022-05-12T00:00:00+08:00
draft: false
tags: ["Linux"]
categories: ["Notes"]

# contentCopyright: MIT
mathjax: true
autoCollapseToc: true
postMetaInFooter: true
reward: false
author: Ren Zhenyu
---

# Linux Summary

## windows双系统干净删除Ubuntu

1. 磁盘管理 删除卷。

2. CMD：

   ```
   diskpart
   list disk
   select disk 0
   list partition
   select partition 1
   assign letter = j
   ```

   ![image-20220512205919353](../linux.assets/image-20220512205919353.png)

3. 管理员权限打开记事本，删除`J/WFI/Ubuntu`文件夹。

   ![image-20220512210227664](../linux.assets/image-20220512210227664.png)

4. CMD `remove letter=j`
