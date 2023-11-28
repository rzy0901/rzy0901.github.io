---
title: "How to use this website"
date: 2023-11-14T18:24:17+08:00
lastmod: 2023-11-14T18:24:17+08:00
draft: false
keywords: []
description: ""
tags: []
categories: []
author: "Ren Zhenyu"

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: true
toc: false
autoCollapseToc: true
postMetaInFooter: true
hiddenFromHomePage: true
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
typora-copy-images-to: ../../static/Usage.assets
typora-root-url: ../../static
---

<!--more-->

## What's new in this theme?

Compared with orignal [even](https://github.com/olOwOlo/hugo-theme-even), my theme added new functions as follows:

1. Dark/Light mode.
2. Solve Mathjax bug (quite important for latex users).
3. Add "print the page as pdf" option (just right click and select "print..." to have a try).
4. Upgrade fancybox gallery to 5.0 for the aim of dark mode compatibility.
5. Some other tiny changes such as excluding some posts from archives...

I don't make a pull request to the original [even](https://github.com/olOwOlo/hugo-theme-even) since the owner seems to be disappeared. And my codes are a little messy that I do not have time to distinguish them into several independent commits.

## Usage

1. First, clone my repsoitory.

   ```
   git clone https://github.com/rzy0901/rzy0901.github.io.git
   ```

2. Use my built `hugo` with goldmark support, which could solve the mathjax bug driven by backslash `\` in your markdown document:

   https://github.com/rzy0901/hugo/releases/tag/v1.0.0

3. If you are using github page to deploy, you can try my github action template [build.yml](https://raw.githubusercontent.com/rzy0901/rzy0901.github.io/main/.github/workflows/build.yml) (You might need to set up a personal token using `Secrets and variables` in your repository settings):

   ![image-20231114183632201](/Usage.assets/image-20231114183632201.png)

4. Run `hugo server` and preview your website at <localhost:1313>.

5. Edit personal informations in `config.toml` and `/themes/even/layouts/_default/baseof.html`.

6. Create a new post, which will generate default flags defined in [default.md](https://raw.githubusercontent.com/rzy0901/rzy0901.github.io/main/themes/even/archetypes/default.md):

   ```
   hugo new post/test.md
   ```

7. I have set the relative filepath just match the local makrdown editor [typora](https://typora.io/) by above [default.md](https://raw.githubusercontent.com/rzy0901/rzy0901.github.io/main/themes/even/archetypes/default.md), so just enjoy typing!

   + Screenshot 1 (image post):
    ![image-20231114185640859](/Usage.assets/image-20231114185640859.png)

   + Screenshot 2 (equation post):

     ![image-20231114185855970](/Usage.assets/image-20231114185855970.png)
