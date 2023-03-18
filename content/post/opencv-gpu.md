---
title: "Ubuntu源码编译Opencv-GPU 4.7.0踩坑记录"
date: 2023-03-12T11:10:39+08:00
lastmod: 2023-03-12T11:10:39+08:00
draft: false
# keywords: []
description: ""
tags: ["opencv"]
categories: ["opencv"]
author: ""

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: true
toc: true
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
# You can also define another contentCopyright. e.g. contentCopyright: "This is another copyright."
contentCopyright: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false

# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false

# You can enable or disable out-of-date content warning for individual post.
# Comment this out to use the global config.
#enableOutdatedInfoWarning: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

<!--more-->

> + 网上安装opencv有很多教程，但是一旦涉及到使用cuda加速的opencv DNN模型等，很多教程就毫无意义，opencv官网2.4k的issues也说明了其bug之多。
>
> + 本文是作者对opencv gpu源码编译的总结。
>
> + 参考教程（有些问题，但是大体思路不错）：<https://learnopencv.com/opencv-dnn-with-gpu-support/>

## 源码编译过程

1. 安装依赖。

   ```
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install build-essential cmake unzip pkg-config
   sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
   sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
   sudo apt-get install libv4l-dev libxvidcore-dev libx264-dev
   sudo apt-get install libgtk-3-dev
   sudo apt-get install libblas-dev liblapack-dev gfortran
   sudo apt-get install python3-dev
   ```

2. CUDA CUDNN安装。网上已经有很多教程，这里不再赘述。

   + 本文使用CUDA 11.6以及CUDNN 8.4.1。
   + 只要CUDA和CUDNN的版本匹配就好了，不需要卸载已经有的版本重新安装，后续源码编译CMakeLists.txt会自动检测最低要求的CUDA和CUDNN要求。

3. 下载并解压opencv及opencv_contrib（注意这个路径，cmake编译时候需要使用）源码到home下：

   ```
   cd ~
   wget -O opencv-4.7.0.zip https://github.com/opencv/opencv/archive/refs/tags/4.7.0.zip
   unzip -q opencv-4.7.0.zip
   mv opencv-4.7.0 opencv
   rm -f opencv-4.7.0.zip 
   ```

   ```
   wget -O opencv_contrib-4.7.0.zip https://github.com/opencv/opencv_contrib/archive/4.7.0.zip
   unzip -q opencv_contrib-4.7.0.zip
   mv opencv_contrib-4.7.0 opencv_contrib
   rm -f opencv_contrib-4.7.0.zip 
   ```

4. 安装numpy：`pip install numpy`。

5. 源码编译opencv：

   ```
   cd ~/opencv
   mkdir build
   cd build
   ```

   + 我习惯使用`cmake-gui`编译，可以更好的选择编译选项：

   ```
   cmake-gui
   ```

   + 默认使用configure。
   + 设置OPENCV_EXTRA_MODULES_PATH为~/opencv_contrib/modules。

   + 勾选OPENCV_ENABLE_NONFREE，WITH_CUDNN，WITH_CUDA，WITH_CUBLAS，BUILD_EXAMPLES（如果勾选这个，我的经验是需要要按照[#22245](https://github.com/opencv/opencv/pull/22245/commits/5acf351e4b9d099d446f401df690d559ed5dfdad)修改`samples/cpp/CMakeLists.txt`，不然会有bug：[21804](https://github.com/opencv/opencv/issues/21804)）等等。
   + configure以后再点击generate。

6. 安装opencv（很慢，有时候会在某个选项卡很久。）

   ```
   make -j `nproc` && sudo make install
   ```

7. 建立软连接。

   ```
   # 本机python3.8的site-pakages
   cd /home/rzy/.local/lib/python3.8/site-packages
   # cv2.so文件安装位置
   ln -s /usr/local/lib/python3.8/site-packages/cv2/python-3.8/cv2.cpython-38-x86_64-linux-gnu.so cv2.so
   ```

8. 现在opencv-gpu就已经安装好了。

## C++，Python代码自动补全vscode设置

![](/opencv-gpu.assets/1.png)

![](/opencv-gpu.assets/2.png)

## C++, Python cuda测试

### 文件结构及测试（下面copy代码）：

```
├── CMakeLists.txt
├── main.cpp
└── main.py
```

+ CPP测试：

  ```
  mkdir build
  cd build
  cmake ..
  make
  ./main
  ```

  ![](/opencv-gpu.assets/3.png)

+ Python测试：`python3 main.py`

  ![](/opencv-gpu.assets/4.png)

### C++测试代码：

`main.cpp`

```c++
#include <iostream>
#include <opencv2/dnn.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <opencv2/core/cuda.hpp>

using namespace std;
using namespace cv;
using namespace dnn;
using namespace cuda;

int main(int, char**) {

    printCudaDeviceInfo(0);

    cout << "Hello, world!\n";
}
```

`CMakelists.txt`

```cmake
cmake_minimum_required(VERSION 3.0.0)
project(main)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(main main.cpp)

target_link_libraries( main ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
```

#### Python测试代码

```python
import cv2
from cv2 import cuda
cuda.printCudaDeviceInfo(0)
```

