---
title: "Notebook for Applied Stochastic Processes"
date: 2022-02-22T00:00:00+08:00
lastmod: 2022-03-04T00:00:00+08:00
draft: false
tags: ["Notes"]
categories: ["Notes"]

# contentCopyright: MIT
mathjax: true
autoCollapseToc: true
postMetaInFooter: true
reward: false
author: Ren Zhenyu (Based on Professor Zhang Yiying's lectures)
---

{{% admonition info "info" %}}

This is a collection of  my notes for SUSTech MA208 "Applied Stochastic Processes", in the spring semester of 2022, based on Professor [Zhang Yiying (张艺赢)](https://sites.google.com/site/yiyingzhang16)'s lectures and slides.

{{% /admonition %}}

# Chapter 1: Preliminaries: Reviews on Probability Theory

## Probability Space

{{% admonition tip"Definition (Probability Space). " %}}The probability space $(\Omega,\mathcal{F},\mathbb{P})$ is defined as follows:

+ $\Omega$: sample space, the set of all possible outcomes.
+ $\mathcal{F}$: $\sigma$-field ($\sigma$-algebra) on $\Omega$ or collection of events.
+ $\mathbb{P}$: Probability measure on $(\Omega,\mathcal{F})$.

{{% /admonition %}}

{{% admonition tip"Definition ($\sigma$-algebra)." %}}

 For a sample space $\Omega$, $\mathcal{F}$ is said to be a $\sigma$-algebra if it satisfies:

+ $\Omega \in \mathcal{F}$;
+ closed under complement, that is, if $E\in \mathcal{F}$, then $E^c \in \mathcal{F}$;
+ closed under countable unions of events, that is, $E_i \in \mathcal{F}$, $i=1,2,\cdots$, then $\cup_iE_i \in \mathcal{F}$.

_Remark_: $\mathcal{F}$ is collection of sets (For example,  $\Omega = \\{a,b,c,d\\}, \mathcal{F}=\\{\emptyset,\Omega,\\{a,b\\},\\{c,d\\}\\}.$

{{% /admonition %}}

{{% admonition tip"Definition (Probability)." %}}

Any event $E \in \Omega$, $\mathbb{P}(E)$ is called the probability of the event $E$ if it satisffies:

+ $0 \leq \mathbb{P}(E) \leq 1$;
+ If $E_i \in \mathcal{F}$, $E_i \cap E_j = \emptyset$ for $i\neq j$ (mutually disjoint events), then $\mathbb{P}(\cup E_i)=\sum_i\mathbb{P}(E_i)$; (概率的可数可加性)
+ $\mathbb{P}(\Omega) = 1$. ($\mathbb{P}(\emptyset) = 0$)

_Remark_: $\mathbb{P}(\cup_iE_i)\leq \sum_i\mathbb{P}(E_i)$ (subadditivitiy property or Boole's inequality).

{{% /admonition %}}

{{% admonition info "Remark (Continuity property of $\mathbb{P}$)." %}}

For a monotone sequence $\\{E_n,n \geq 1\\}$,  if and only if $\lim\limits_{n\to \infty}\mathbb{P}(E_n)=\mathbb{P}(\lim\limits_{n \to \infty}E_n)$. 

+ (Increasing sequence). If $E_1 \subset E_2 \subset \cdots$, then $\lim\limits_{n\to \infty}\mathbb{P}(E_n)=\mathbb{P}(\lim\limits_{n \to \infty}E_n)=\mathbb{P}(\cup_{n=1}^{\infty}E_n)$.

+ (Decreasing sequence). If  $E_1 \supset E_2 \supset \cdots$, then $\lim\limits_{n\to \infty}\mathbb{P}(E_n)=\mathbb{P}(\lim\limits_{n \to \infty}E_n)=\mathbb{P}(\cap_{n=1}^{\infty}E_n)$.

{{% /admonition %}}

{{% admonition tip"Definition (Infimum and Supremum, 上下确界)." %}}

 Suppose $\\{A_n\\}_{n=1}^{\infty}$ is a sequence of sets. 

Define：
$$
\text{(All except finitely often, a.e.f.o.)} \quad
\lim_\limits{n\to \infty}\inf A_n = \cup_{n\geq 1}\cap_{j 
\geq n}A_j
$$
and
$$
\text{(Infinitely Often, i.o.)} \quad \lim\limits_{n \to \infty}\sup A_n = \cap_{n \geq 1}\cup_{j \geq n} A_j
$$

***

_Remark_: 

+ (a.e.f.o) 


$$
\begin{aligned}
&x \in \lim_\limits{n\to \infty}\inf A_n = \cup_{n\geq 1}\cap_{j \geq n}A_j  
\newline &\Longleftrightarrow \exists n_i,x \in \cap_{j \geq n_i}A_j, \text{for some } i
\newline &\Longleftrightarrow \exists n_i,x \in A_{n_i},A_{n_{i+1}}\cdots,A_{\infty}
\end{aligned}
$$

+ (i.o.)
  $$
  \begin{aligned}&x \in \lim_\limits{n\to \infty}\sup A_n = \cap_{n\geq 1}\cup_{j \geq n}A_j  
  \newline &\Longleftrightarrow \forall n,x \in \cup_{j \geq n}A_j
  \newline &\Longleftrightarrow \forall n, \exists m\geq n, x \in A_m
  \end{aligned}
  $$



***

_Simple Proof_: (Why the infimum and superemum is defined as above?)

Let $L_n=\cap_{j\geq n}A_j$, $U_n = \cup_{j\geq n}A_j$, then $L_n \leq A_n \leq U_n$.

Taking $\lim\limits_{n\to\infty}$ we have: $\lim\limits_{n\to\infty}L_n \leq \lim\limits_{n\to\infty}A_n \leq \lim\limits_{n\to\infty} U_n$.

Since  $\\{L_n\\}$ and $\\{U_n\\}$ are monotonically increasing and decreasing sequences seperately, by the continuity property of $\mathbb{P}$, we have:
$$
\underbrace{\lim\limits_{n\to\infty}\cup_{n\geq1}\cap_{j\geq n}A_j}_{\lim_\limits{n\to \infty}\inf A_n} \leq \lim\limits_{n\to\infty}A_n \leq \underbrace{\lim\limits_{n\to\infty}\cap_{n\geq1}\cup_{j\geq n}A_j}_{\lim_\limits{n\to \infty}\sup A_n}
$$
{{% /admonition %}}

{{% admonition info "Proposition (Borel-Cantelli Lemma)"%}}

Let  $E_1,E_2,\cdots$ denote a sequence of events, define 
$$
\lim\limits_{n \to \infty}\sup E_n = \cap_{n=0}^{\infty} \cup_{i=n}^{\infty}E_i=\\{\text{an infinite number of }E_i \text{ occur}\\}.
$$

+ **Proposition** **(Borel-Cantelli Lemma I).** If $\sum_{i=1}^\infty\mathbb{P}(E_i)<\infty$, then
  $$
  \mathbb{P}(\lim\limits_{n \to \infty}\sup E_n)=\mathbb{P}(\text{an infinite number of }E_i \text{ occur})=0.
  $$
  
  Proof. 
  
  $$
  \begin{align}
  &\mathbb{P}(\lim\limits_{n \to \infty}\sup E_n) = \mathbb{P}(\cap_{n=0}^{\infty} \cup_{i=n}^{\infty}E_i) \newline
  &\xlongequal[]{\text{since } \cup_{i=n}^{\infty}E_i \text{ is decreasing.}} \mathbb{P}(\lim_\limits{n \to \infty}\cup_{i=n}^{\infty}E_i)=\lim_\limits{n \to \infty}\mathbb{P} (\cup_{i=n}^{\infty}E_i) \newline
  & \leq \lim_\limits{n \to \infty} \sum_{i=n}^{\infty}\mathbb{P}(E_i) \stackrel{(a)}{=} 0,
  \end{align}
  $$
  
  where $(a)$ holds because of $\sum_{i=1}^\infty\mathbb{P}(E_i)<\infty$. (Proof is straightforward by taking $\lim\limits_{n \to \infty}$ at both sides of $\sum_{i=1}^\infty\mathbb{P}(E_i) = \sum_{i=1}^{n-1}\mathbb{P}(E_i)+\sum_{i=n}^\infty\mathbb{P}(E_i)$.)
  
+  **Proposition** **(Borel-Cantelli Lemma II).** If $E_1,E_2,\cdots$ are independent events such that $\sum_{i=1}^\infty\mathbb{P}(E_i)=\infty$, then 
  $$
  \mathbb{P}(\lim\limits_{n \to \infty}\sup E_n)=\mathbb{P}(\text{an infinite number of }E_i \text{ occur})=1.
  $$
  Proof. For any $n<m<\infty$, since $1-x<e^{-x}$,
  $$
  \begin{align}
  &\mathbb{P}(\left(\cup_{i=n}^{m}E_i\right)^c)=\mathbb{P}(\cap_{i=n}^{m}E_i^c)=\prod_{i=n}^m \mathbb{P} (E_i^c) \text{ (By independence)} \newline
  &= \prod_{i=n}^m (1-\mathbb{P}(E_i)) \leq \prod_{i=n}^m \exp(-\mathbb{P}(E_i))=\exp\left(-\sum_{i=n}^m \mathbb{P}(E_i)\right) \stackrel{m \rightarrow \infty}{\longrightarrow} 0,
  \end{align}
  $$
  which means that $\mathbb{P}(\cup_{i=n}^{m}E_i)\to 1$ as $m \to 0$, $\mathbb{P}(\cup_{i=n}^{\infty}E_i)=1$ for any $n$. Hence,
  $$
  \mathbb{P}(\lim\limits_{n \to \infty}\sup E_n) = \mathbb{P}(\cap_{n=0}^{\infty} \cup_{i=n}^{\infty}E_i) 
  = \mathbb{P}(\lim_\limits{n \to \infty}\cup_{i=n}^{\infty}E_i)=\lim_\limits{n \to \infty}\mathbb{P} (\cup_{i=n}^{\infty}E_i)=1.
  $$

{{% /admonition %}}

+ (容斥原理，Inclusion-exclusion Principle): $A_1,A_2,\dots,A_n$ are events, then:
  $$
  \mathbb{P}\left(\cup_{i=1}^{n} A_{i}\right)=\sum_{i=1}^{n} \mathbb{P}\left(A_{i}\right)-\sum_{i<j} \mathbb{P}\left(A_{i} A_{j}\right)+\sum_{i<j<k} \mathbb{P}\left(A_{i} A_{j} A_{k}\right) 
  -\cdots+(-1)^{n+1} \mathbb{P}\left(A_{1} \cdots A_{n}\right).
  $$

+ 
  $$
  \mathbb{P}(\text{exactly } r  \text{ of the events }  A_{1}, \cdots, A_{n}\text{ occur})
  =\sum_{i=0}^{n-r}(-1)^{i}\left(\begin{array}{c}
  r+i \newline
  r
  \end{array}\right) \sum_{j_{1}<j_{2}<\cdots<j_{r+i}} \mathbb{P}\left(A_{j_{1}} A_{j_{2}} \cdots A_{j_{r+i}}\right).
  $$

## Random Variable and Distributions

{{% admonition tip "Definition (random variable, distribution function)" %}}

A **random variable** $X$ is a mapping from $\Omega$ to $\mathbb{R}$, and for any Borel Set $A\subset \mathbb{R}$ (这里等价认为，$(-\infty,a],\forall a \in \mathbb{R}$),
$$
\mathbb{P}(X(\omega)\in A) = \mathbb{P}(X^{-1}(A))=\mathbb{P}\\{\omega:X(\omega)\in A\\}.
$$
The **distribution function** $F$ of a random variable $X$ is defined for any real number $x \in \mathbb{R}$,
$$
F(x) = \mathbb{P}(X \leq x)=\mathbb{P}(X \in (-\infty,x]),
$$
 and the **survival (or tail) function** is $\overline{F}(x)=1-F(x)=\mathbb{P}(X > x)$.

***

Properties of distribution function:

+ Right-continous; Non-decreasing ($\lim_\limits{x\to+\infty}F(x)=1,\lim_\limits{x\to-\infty}F(x)=0$);
+ If $X$ is discrete random varibale, $F(x)=\sum_{z\leq x}\mathbb{P}(x)$. If $X$ takes uncountably many values, summation makes NO sense.

***

**(Continuous Random Variable).** $X$ is said to be a continuous random variable if there exists a function $f(x)$ such that for any Borel set $B \subset \mathbb{R}$,
$$
\mathbb{P}(X \subset B)=\int_Bf(x)dx.
$$
$f(x)$ is called the probability density function (pdf). For continuous r.v. $X$,
$$
F(x) = \int_{-\infty}^xf(y)dy
$$
and 
$$
f(x) = F^{\prime} (x).
$$

***

**(Joint distribution).** For random variables $X$, $Y$ , the joint distribution is defined by
$$
F(x,y)=\mathbb{P}(X\leq x,Y \leq y).
$$
Correspondingly, the distributions (marginal distributions) of $X,Y$ are:
$$
\begin{align}
F_X(x)=\mathbb{P}(X\leq x)=\lim\limits_{y \to \infty}\mathbb{P}(X\leq x, Y \leq y)=\lim\limits_{y \to \infty}F(x,y) \newline
F_Y(y)=\mathbb{P}(Y\leq y)=\lim\limits_{x \to \infty}\mathbb{P}(X\leq x, Y \leq y)=\lim\limits_{x \to \infty}F(x,y)
\end{align}
$$
{{% /admonition %}} 

## Expectations



# 关于本博客撰写的一些统一规范

关于Mathjex结合markdown使用Latex的bug记录:

```html
一、集合\{\}的转义问题: $\{\}$需要写为$\\{\\}$
二、公式换行：必须使用\begin{aligned} \newline \end{aligned}或\begin{align} \newline \end{align}
```

Adomonition文本框，撰写规范: 

```html
一、Definition 使用 \{\{% admonition tip "Definition XXX" %\}\} \{\{% /admonition tip %\}\}
二、Proposition, Remark 使用 \{\{% admonition tip "Definition XXX" %\}\} \{\{% /admonition tip %\}\}
```



