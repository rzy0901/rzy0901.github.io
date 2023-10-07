---
title: "Wireless Channel Trouble-Shooting"
date: 2023-10-07T00:00:00+08:00
draft: false
tags: ["Math","Wireless Communication","Channel Model"]
categories: ["Math"]

contentCopyright: MIT
mathjax: true
autoCollapseToc: false
postMetaInFooter: true
reward: false
author: Ren Zhenyu
typora-copy-images-to: ../../static/channel.assets
typora-root-url: ../../static
---

>**DISCLAIMER:** This note is for reference only. I am not 100% sure of the accuracy of my note. If you find any errors/typos, feel free to contact me.
>
>This note records some interesting issues that I met in wireless channel modeling :smile:.

# CIR, CFR (CSI) Conversion

<center><img src="/channel.assets/channel.png" alt="channel" style="zoom: 20%;" /></center>

+ Channel Impulse Response (CIR): $h(t,\tau)$; Channel Frequency Response (CFR): $H(t,f)$.

  + $t$: time domain; $\tau$: delay domain; $f$: frequency domain.

  + Discrete Fourier Transform (DFT), Inverse Discrete Fourier Transform (IDFT) formula:
    $$
    \begin{cases}
    X[k]=\sum_{n=0}^{N-1}x[n]\exp\left(-\frac{\mathrm{j}2\pi kn}{N}\right)\\=\sum_{n=-\infty}^{\infty}x[n]\exp(-\mathrm j \omega n)|_{\omega=2\pi k/N}=X(e^{\mathrm j\omega})|_{\omega=2\pi k/N}\\
    x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]\exp\left(\frac{\mathrm j 2\pi kn}{N}\right)
    \end{cases}
    $$

  + Simple proof (Considering CIR/CFR at one time slot $t$):

    > Note that $f_n=n\Delta f$, $\tau_n=n\Delta t$, $\Delta f\Delta t=1/N$. (Take a look at above DFT equations or time/frequency settings in  [MATLAB Fast Fourier Transform (fft) documentation](https://www.mathworks.com/help/matlab/ref/fft.html) example codes. )

    We have CIR in below form:
    $$
    h(\tau)=\sum_{i=0}^{N-1}\alpha_0\delta(\tau-\tau_i)\rightarrow \mathbf{h}=[\alpha_0,\ldots,\alpha_{N-1}],
    $$

    Do DFT at $k$:                                                                                                                      
    $$
    H(k)=\sum_{n=0}^{N-1}\alpha_n\exp(-\frac{\mathrm{j2\pi kn}}{N})
    $$
    
    Substitute $k$ with $f$ at the left of, and substitute $k$ with $f/\Delta f$ at the right side of the equation, we have:
    $$
    \begin{aligned}
    H(f)&=\sum_{n=0}^{N-1}\alpha_n\exp(-\frac{\mathrm{j2\pi f/\Delta f n}}{N}) \\
    &\xlongequal[]{\Delta f =1/(N\Delta t)}\sum_{n=0}^{N-1}\alpha_n\exp(-\mathrm{j2\pi f\tau_n})
    \end{aligned}
    $$

+ Channel State Information (CSI): $H(t,f)$. (CSI is actually discrete time series of discrete CFR!)

  + $t$: CSI packet timestamp.
  + $f$: OFDM subcarrier frequency.
  + Sometimes there is an extra space dimension in CSI Matrix which refers to Tx and Rx antenna pairs.

+ 一个靠谱的知乎问题：[在通信专业里的时域，频域，空域，角域到底都有怎样的联系呢？](https://www.zhihu.com/question/315208907/answer/2742955196)

# Wideband/Narrowband Channel Models

To be updated tomorrow (2023.10.8)...
