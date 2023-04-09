---
title: "在Hugo theme-even上简单实现暗黑模式"
date: 2022-11-05T00:00:00+08:00
# lastmod: 2022-11-05T00:00:00+08:00
draft: false
tags: ["Hugo"]
categories: ["diary"]

# contentCopyright: MIT
mathjax: true
autoCollapseToc: false
postMetaInFooter: true
reward: true
author: Ren Zhenyu
typora-root-url: ./..\..\static
---

# 暗黑模式介绍

> + Hugo的[even](https://github.com/olOwOlo/hugo-theme-even)主题在github已经两年没有更新了，我应该是第一个为该主题提供暗黑模式的人（~~但是由于在手机端还有bug，我暂时还不想发起pull request，不过大家可以随便的copy我的代码并做出改进发起PR:smile:。~~）
>
> + <font color =  "red">**2023.4.10更新：** 添加了移动端的暗黑模式显示，见[commit: update mobile dark mode](https://github.com/rzy0901/rzy0901.github.io/commit/1c4874d94dd61f918c7fd27edd6574b379abfd23)，这意味着暗黑模式的全部bug已经得到解决，有时间我打算向[even](https://github.com/olOwOlo/hugo-theme-even)发起PR（虽然似乎even的作者失踪了）。</font>
>
> + 最近试了很多方法，终于简单的在浏览器端实现了dark mode（点击右上角导航栏里的图标即可）。
>
>   <img src="/dark-mode.assets/200128941-81d53c52-010f-4bd6-9dc7-5933291c5ecd.png" alt="image" style="zoom: 50%;" />

![](/dark-mode.assets/GIF.gif)

# 零前端基础具体代码实现 (Copy!)

作为一个只会`matlab`和`cpp`语言的通信人，**在零css，js等计算机前端基础下**，我是怎么实现的呢？答案很简单，就是不断的copy代码，像写`latex`一样地写网页。

首先，我们注意到chrome浏览器中有一个很好用的插件, 这意味着我们只要copy这个插件的源码就可以了。所以我实现的代码流程如下（具体间[commit: Add Dark Theme feature.](https://github.com/rzy0901/rzy0901.github.io/commit/c08c69da33ab361368fcb64dba066c15dd6d5fbd)）：

1. 为even主题`/themes/even/layouts/partials/head.html`添加`fontawsome`的`css`代码（之前有试过官网推荐的引用js代码的方式，虽然也可行，但是加载太慢，不推荐）:
```html
<link href="https://cdn.bootcdn.net/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
```
> 上述方法使用`font-awsome`的CDN，如果CDN挂了就g了，所以我将`font-awsome`部署到了本地：
>
> + 在[官方教程](https://fontawesome.com/v4/get-started/)之下下载`font-awesome-4.7.0`文件夹，将其放置于`/themes/even/static/css/`之下，在`head.html`添加如下代码：
>
>   ```html
>   <link rel="stylesheet" href = "/css/font-awesome-4.7.0/css/font-awesome.css"></link>
>   ```

2. 安装[dark mode](https://mybrowseraddon.com/dark-mode.html)，在本机`C:\Users\RZY\AppData\Local\Google\Chrome\User Data\Default\Extensions\dmghijelimhndkbmpgbldicpogfkceaj\0.4.6_0\data\content_script\general`处选择自己喜欢的`dark.css`，拷贝到`/themes/even/static/css/`下，并在`/themes/even/layouts/partials/head.html`下添加以下代码：

```html
<link disabled id="dark-mode-theme" rel="stylesheet" href="/css/dark.css"></link>
```

3. 在`/themes/even/layouts/partials/header.html`的`menu`中添加切换暗黑模式的图标：

```html
<li class="menu-item">
    <a id="dark-mode-toggle" class="menu-item-link">
      <i id="dark-mode-toggle-i" class="fa fa-moon-o"></i>
    </a>
</li>
```

4. 在`/themes/even/layouts/partials/scripts.html`添加以下js代码（网上copy的代码[^1]），

```html
<script>
  //通过时间判断夜间模式，否则会完全手动切换并本地持久化模式，下次自动渲染本地持久化的模式
var darkMode = {
  config:{    
    startHour:19,//19点开始
    endHour:7,//7点结束    
  },
  _darkTheme:null,  //dark.css标签
  _modeToggle:null, //手动切换按钮块
  _modeToggleParent:null, //手动切换按钮wrap
  _currentHour:0, //当前小时
  _storageKey:"dark-mode-storage",
  _storageByHandLastTIme:0, //上次手动设置模式时间 毫秒
  _storageOverdueHours:12,  //每隔12小时重新检查本地持久化

  init:function(){
    //夜间模式切换配置
    this._modeToggleParent = document.getElementById("dark-mode-toggle");
    this._modeToggle = document.getElementById("dark-mode-toggle-i");    
    this._darkTheme = document.getElementById("dark-mode-theme");  
    this._currentHour = new Date().getHours();  

    this.toggleListen();
    this.initMode();
  },
  initMode:function(){
    //初始化模式，来源本地持久化或自动检测模式    
    let initMode = this.getModeFromStorage() || this.autoMode(); 
    this.setMode(initMode);
  },
  toggleListen:function(){
    let _this = this;
    //手动切换触发模式更改
    this._modeToggleParent.addEventListener("click", () => {
        if (this._modeToggle.className === "fa fa-moon-o") {
            _this.setModeByHand("dark");
        } else if (this._modeToggle.className === "fa fa-sun-o") {
            _this.setModeByHand("light");
        }
    });

  },  
  autoMode:function(){
    let _currentHour = this._currentHour;
    if(_currentHour > this.config.startHour || _currentHour < this.config.endHour){
      return "dark";  
    }  
    return "light";    
  },
  setMode:function(mode){
    if (mode === "dark") {
        this._darkTheme.disabled = false;
        this._modeToggle.className = "fa fa-sun-o";
    } else if (mode === "light") {
        this._darkTheme.disabled = true;
        this._modeToggle.className = "fa fa-moon-o";
    }          
  },
  setModeByHand:function(mode){
    this.setMode(mode);
    this.setModeToStorage(mode);    
  },
  setModeToStorage:function(mode){
    localStorage.setItem(this._storageKey, mode);
    localStorage.setItem(this._storageKey+"-last-time", (new Date().getTime()));     
  },
  getModeFromStorage:function(){
    let _mode = localStorage.getItem(this._storageKey);
    let _lastSetTime = localStorage.getItem(this._storageKey+"-last-time");
    if(_mode && _lastSetTime){
      _lastSetTime = _lastSetTime/1000;
      let _currentTime = new Date().getTime()/1000;
      let _overdueSeconds = this._storageOverdueHours * 3600;
      if(_currentTime - _lastSetTime < _overdueSeconds){            
        return _mode;
      }
    }
    localStorage.removeItem(this._storageKey);
    localStorage.removeItem(this._storageKey+"-last-time");
    return false;

  },
};
darkMode.init();
</script> 
```

[^1]:https://zhuanlan.zhihu.com/p/363949798
