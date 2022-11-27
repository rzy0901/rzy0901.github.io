---
title: "A trick to fix Hugo Mathjax bugs: \\$\\{\\}\\$ display error"
date: 2022-11-27T13:49:19+08:00
lastmod: 2022-11-27T13:49:19+08:00
draft: false
tags: ["hugo","mathjax"]
categories: []
author: ""
mathjax: true
autoCollapseToc: true
postMetaInFooter: true
reward: false
# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false
---

## Brief Bug Descirption

+ See the output of following text:

```markdown
We know $\mathcal{A}= \{a_1,a_2,a_3\}$ is a set.

$$
\mathcal{A}= \{a_1,a_2,a_3\}
$$
```

+ Output (\\{\\} is not recognized!):

> We know $\mathcal{A}= \{a_1,a_2,a_3\}$ is a set.
> $$
> \mathcal{A}= \{a_1,a_2,a_3\}
> $$

## How to get the desired output?

+ Simply to use `<div></div>` to render the markdown as html! 

```markdowns
<div style ="display: inline;">We know $\mathcal{A}= \{a_1,a_2,a_3\}$ is a set.</div> 

<div>
$$
\mathcal{A}= \{a_1,a_2,a_3\}
$$
</div>
```

> <div style ="display: inline;">We know $\mathcal{A}= \{a_1,a_2,a_3\}$ is a set.</div> 
> 
> <div>
> $$
> \mathcal{A}= \{a_1,a_2,a_3\}
> $$
> </div>