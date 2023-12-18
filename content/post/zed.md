---
title: "基于深度摄像机ZED 2i提取导出三维人体骨骼"
date: 2022-10-14T00:00:00+08:00
lastmod: 2022-11-26T00:00:00+08:00
draft: false
tags: ["Linux","OpenPose","3d skeletons","opencv"]
categories: ["Notes"]

# contentCopyright: MIT
mathjax: true
autoCollapseToc: false
postMetaInFooter: true
reward: false
author: Ren Zhenyu
typora-copy-images-to: ../../static/zed.assets
typora-root-url: ../../static
---


> + ZED SDK 安装，功能参考实现链接：[ZED SDK Documentations](https://www.stereolabs.com/docs/)以及[Body Tracking Overview](https://www.stereolabs.com/docs/body-tracking/)。
> + 3D Body Tracking需要CUDA11.1以上的版本(本文测试于CUDA11.6)以及ZED 2以上的深度摄像机（本文使用ZED 2i测试）。
> + 如果电脑是双显卡，需设置Nvidia显卡为Primary GPU，参考：[How can I solve OpenGL issues under Ubuntu?](https://support.stereolabs.com/hc/en-us/articles/8422008229143-How-can-I-solve-OpenGL-issues-under-Ubuntu-)。

## ZED 视频录制以及对视频后验处理流程

1. 连接摄像头，首先在`/usr/local/zed/tools/`中选择ZED_Explorer软件进行录制。

   + 如果需要脚本控制录屏，可参考ZED SDK安装目录下的示例代码`/usr/local/zed/samples/svo\ recording/`中的cpp或python代码。
     + `/usr/local/zed/samples/`中还有很多其他示例代码，如果安装SDK时未下载，可在[zed-examples](https://github.com/stereolabs/zed-examples)获取。

2. 录制好的`.svo`文件会默认存放在`/home/<username>/Documents/ZED`下。

3. 对录制好的`.svo`进行后续处理，[官方给的实时处理代码](https://github.com/stereolabs/zed-examples/tree/master/body%20tracking)不太好用，这里我进行了二次编程将三维关节点数据，以及每一祯对应的timestamp导出为MATLAB支持的`.mat`文件（代码见[testZED](https://github.com/rzy0901/testZED)）。

   > 为什么不使用官方的实时处理代码：
   >
   > + 官方的实时处理代码并没有将keypoints导出到文件。
   > + 即使对实时处理的代码再次编程导出keypoints信息，由于实时处理的特性，大量祯的keypoints信息会被丢弃，而估计出的timestamp由于代码处理时间过长也会出错。
   > + 先录制`.svo`文件，后验的处理`.svo`不会出现以上问题。

## 处理结果

> 2022-11-26 更新：安装最新的SDK并在安装时选择对模型进行优化，可以得到更好的tracking效果。

+ 将.dat导入MATLAB处理结果：

  + Walk:

    | ![](https://github.com/rzy0901/testZED/blob/main/README.assets/walk1.gif?raw=true) | ![](https://github.com/rzy0901/testZED/blob/main/README.assets/walk2.gif?raw=true) |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |

  + Run：
  
    | ![](https://github.com/rzy0901/testZED/blob/main/README.assets/run1.gif?raw=true) | ![](https://github.com/rzy0901/testZED/blob/main/README.assets/run2.gif?raw=true) |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
  
  + Squat:
  
    |![](https://github.com/rzy0901/testZED/blob/main/README.assets/squat.gif?raw=true)|
    | ------------------------------------------------------------ |
  
    



## 彩蛋：一个男子在打拳

<center><img src="/zed.assets/lqr.png" alt="test1" style="zoom:25%;" /></center>

</br>
<center>
<img src="/zed.assets/test2.gif" alt="test2" style="zoom: 50%;" />
</center>