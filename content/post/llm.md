---
title: "Large Language Model (LLM) Notes"
date: 2024-03-20T15:08:24+08:00
lastmod: 2024-03-20T15:08:24+08:00
draft: false
keywords: []
description: ""
tags: ["notes","math","llM"]
categories: ["notes"]
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
mathjaxEnableAutoNumber: false

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
typora-copy-images-to: ../../static/llm.assets
typora-root-url: ../../static
---

<!--more-->

> Based on [https://llm-course.github.io](https://llm-course.github.io/).

## Basics

### Language Model

A language model assigns probability to $N$-gram: $f:V^n \rightarrow R^+$.

A conditional language model assigns probability to a word given some conditioning context: 

$$
g:(V^{n-1},V)\rightarrow R^{+}.
$$

$$
p(w_n|w_1,\ldots,w_{n-1}) = g(w_1,\ldots,w_{n-1},w) = \frac{f(w_1,\ldots,w_{n})}{f(w_1,\ldots,w_{n-1})}.
$$

A probabilistic model that assigns a probability to every finite sequence (grammatical or not):
$$
P(\text{I am noob})=\underbrace{P(\text{I})*P(\text{am}|\text{I})}_{P(\text{I am})}*P(\text{noob}|\text{I am}).
$$
Decoder-only models (GPT-x models).

Encoder-only models (BERT, RoBERTa, ELECTRA).

Encoder-decoder models (T5, BART).

### language modeling with $n$-gram

{{% admonition%}}

**Definition for $n$-gram:**

An $n$-gram language model assumes each word depends only on the last $n−1$ words (markov assumptions with order $n-1$​):
$$
\begin{align}
P_{ngram}(w_1,\ldots,w_N)&=P(w_1)P(w_2|w_1)\ldots P(w_i|\underbrace{w_{i-1},\ldots,w_{i-(n+1)})}_{n-1 \text{ items}}\ldots P(w_N|w_{N-1},\ldots,w_{N-(n+1)}))\\
&=\prod_{i=1}^N P(w_i|w_{i-1},\ldots,w_{i-(n+1)}).
\end{align}
$$

+ Use EOS (end-of-sentence) `</s>` token to limit sentence length.
+ Add $n-1$ beginning-of-sentence (BOS) (`<s>`) to each sentence for an $n$-gram mode to ensure consistency for $P(w_i|w_{i-1},\ldots,w_{i-(n+1))}$ for the first $n-1$ items.

***

+ Unigram model ($1$-gram​): $P(w_1,\ldots,w_i)=\prod_{k=1}^iP(w_k)$.
+ Bigram model ($2$-gram): $P(w_1,\ldots,w_i)=\prod_{k=1}^iP(w_k|w_{k-1})$.
+ Trigram model ($3$-gram): $P(w_1,\ldots,w_i)=\prod_{k=1}^iP(w_k|w_{k-1},w_{k-2})$​.

{{% /admonition %}}

### Evaluation

{{% admonition %}} 

**(Intrinsic Evaluation). Perplexity:** 

Inverse ($1\over P(\ldots)$) of the probability of the test set, normalized ($\sqrt[N]{\ldots}$) by the # of tokens ($N$) in the test set. 

If a LM assigns probability $P(w_1,\ldots,w_N)$ to a test corpus $w_1,\ldots,w_N$, the perplexity for $n$-gram language model could be written as:
$$
PP(w_1,\ldots,w_N)=\sqrt[N]{1 \over P(w_1,\ldots,w_N)}=\sqrt[N]{1 \over \prod_{i=1}^N P(w_i|w_{i-1},\ldots,w_{i-(n+1)})}.
$$
Rewrite it into log-form (exponent of mean of log likelihood of all the words in an input sequence):
$$
PPL(w_1,\ldots,w_N)=\exp\left(-\frac{1}{N}\sum_{i=1}^N\log\left(P(w_i|w_{i-1},\ldots,w_{i-(n+1)})\right)\right).
$$

+ Lower perplexity $\rightarrow$ a higher probability to the unseen test corpus.

{{% /admonition %}}

{{% admonition %}}

**(Extrinsic Evaluation). Word error rate (WER):**
$$
\text{WER} = \frac{\text{Insertions}+\text{Deletions}+\text{Substitutions}}{\text{Actual words in transcript}}.
$$
{{% /admonition %}}


### ChatGPT

+ Phase 1: pre-training: Learn general world knowledge, ability, etc.
+ Phase 2: Supervised finetuning: Tailor to tasks (unlock some abilities) .
+ Phase 3: Reinforcement Learning and Human Feedback (RLHF).
  + [ChatGPT 背后的“功臣”——RLHF 技术详解](https://huggingface.co/blog/zh/rlhf)

## Resource

ChatGPT API key: <http://eylink.cn>

课程：<https://github.com/mlabonne/llm-course>，<https://llm-course.github.io>

学者：
+ （通信）黄川，hongyang du，
+ Open AI and famous guys, Lilian Weng, Yao Fu, Jianlin Su

图片$\rightarrow$文字：llava

大模型做network调度：netllm

大模型微调：LoRA

