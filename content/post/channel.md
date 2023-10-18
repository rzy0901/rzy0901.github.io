---
title: "Wireless Channel Trouble-Shooting"
date: 2023-10-07T00:00:00+08:00
draft: false
tags: ["Math","Wireless Communication","Channel Model"]
categories: ["Math"]

contentCopyright: MIT
mathjax: true
mathjaxEnableAutoNumber: true
autoCollapseToc: true
postMetaInFooter: true
reward: false
author: Ren Zhenyu
typora-copy-images-to: ../../static/channel.assets
typora-root-url: ../../static
---

>**DISCLAIMER:** This note is for reference only. I am not 100% sure of the accuracy of my note. If you find any mistakes/typos, feel free to contact me.
>
>This note records some interesting issues that I met in wireless channel modeling :smile:.

# CIR, CFR (CSI) Conversion

<center><img src="/channel.assets/channel.png" alt="channel" style="zoom: 20%;" /></center>

+ Channel Impulse Response (CIR): $h(t,\tau)$; Channel Frequency Response (CFR): $H(t,f)$.

  + $t$: time domain; $\tau$: delay domain; $f$: frequency domain.

  + Discrete Fourier Transform (DFT), Inverse Discrete Fourier Transform (IDFT) formula:
    $$
    \begin{equation}
    \begin{cases}
    X[k]=\sum_{n=0}^{N-1}x[n]\exp\left(-\frac{\mathrm{j}2\pi kn}{N}\right)\\=\sum_{n=-\infty}^{\infty}x[n]\exp(-\mathrm j \omega n)|_{\omega=2\pi k/N}=X(e^{\mathrm j\omega})|_{\omega=2\pi k/N}\\
    x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]\exp\left(\frac{\mathrm j 2\pi kn}{N}\right)
    \end{cases}.
    \label{eq:DFT}
    \end{equation}
    $$
    
  + Simple proof (Considering CIR/CFR at one time slot $t$):

    > Note that $f_n=n\Delta f$, $\tau_n=n\Delta t$, $\Delta f\Delta t=1/N$. (Take a look at above DFT equations or time/frequency settings in  [MATLAB Fast Fourier Transform (fft) documentation](https://www.mathworks.com/help/matlab/ref/fft.html) example codes. )

    We have CIR in below form:
    $$
    h(t,\tau)=\sum_{n=0}^{N(t)-1}\alpha_n(t)\delta(\tau-\tau_n(t))\rightarrow \mathbf{h}=[\alpha_0(t),\ldots,\alpha_{N-1}(t)].
    $$

    Do DFT at $k$ using $\eqref{eq:DFT}$:                                                                                                                      
    $$
    H(t,k)=\sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\frac{\mathrm{j2\pi kn}}{N}).
    $$

    Substitute $k$ with $f$ at the left of the equation, and substitute $k$ with $f/\Delta f$ at the right side of the equation, we have:
    $$
    \begin{align}
    H(t,f)&=\sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\frac{\mathrm{j2\pi f/\Delta f n}}{N}), \nonumber \\
    &\xlongequal[]{\Delta f =1/(N\Delta t)}\sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\mathrm{j2\pi f\tau_n(t)}).
    \label{eq:CFR}
    \end{align}
    $$

+ Channel State Information (CSI): $H(t,f)$. (CSI is actually discrete time series of discrete CFR!)

  + $t$: CSI packet timestamp.
  + $f$: OFDM subcarrier frequency.
  + Sometimes there is an extra space dimension in CSI Matrix which refers to Tx and Rx antenna pairs.

+ 一个靠谱的知乎问题：[在通信专业里的时域，频域，空域，角域到底都有怎样的联系呢？](https://www.zhihu.com/question/315208907/answer/2742955196)

# Real Bandpass Signals, Equivalent Complex Baseband (Lowpass) Signals Conversion

## Definition

+ **Real** bandpass signal:
  $$
  \begin{align}
  s(t)=s_\text{I}(t)\cos(2\pi f_\text{c} t) -s_\text{Q}(2\pi f_\text{c} t).
  \end{align}
  $$
  
  + $s_\text{I}(t)$: lowpass in phase component.
  + $s_\text{Q}(t)$: lowpass quadrature component.

  > Many involved signals in wireless communication are always bandpass signal with carrier frequency $f_\text{c}$ and bandwidth $2B$, with $2B \ll f_\text{c}$.
  
+ Equivalent **complex** baseband (lowpass) signal (real bandpass $\rightarrow$ complex baseband):
  $$
  \begin{align}
  u(t)=s_\text{I}(t)+\mathrm{j}s_\text{Q}(t).
  \end{align}
  $$
  
+ Complex baseband $\rightarrow$ real bandpass:
  $$
  \begin{align}
  \text{Real bandpass signal} &= \text{Re}\{\text{Complex baseband signal}\times\exp(\mathrm j2\pi f_\text{c}t)\}, \nonumber \\
  s(t) &= \text{Re}\{u(t)\times\exp(\mathrm j2\pi f_\text{c}t)\}.
  \label{eq:complex2real}
  \end{align}
  $$

## Two types of CIR: Real Bandpass Channel, Equivalent Complex Baseband (Lowpass) Channel

## Channel impulse response

+ Real bandpass channel:
  $$
  \begin{align}
  h_\text{real}(t,\tau)=\sum_{n=0}^{N(t)-1}\alpha_{n}(t)\delta(\tau-\tau_n(t)),
  \label{eq:ch_real}
  \end{align}
  $$
  where:
  
  + $t$ and $\tau$: time domain and delay domain.
  
  + $N(t)$: number of multipaths at time slot $t$.
  + $\alpha_n(t)$ and $\tau_n(t)$: path loss (amplitude) and delay for $n$-th path at time slot $t$.
  
+ Equivalent complex baseband (lowpass) channel:
  $$
  \begin{align}
  h_\text{complex}(t,\tau)=\sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\mathrm{j}\phi_n(t))\delta(\tau-\tau_n(t)),
  \label{eq:ch_complex}
  \end{align}
  $$
  
  where $\phi_n(t)=2\pi f_\text{c} \tau_n(t)-\phi_{\text{D}_n}(t)$ denotes the phase of $n$-th path at time slot $t$, with $\phi_{\text{D}_n}(t)$ denotes the Doppler phase shift.
  
  + Doppler phase shift $\phi_{\text{D}_n}(t)$ is a function of Doppler frequency $f_{\text{D}_n}(t)$: $\phi_{\text{D}_n}(t)=\int_t 2\pi f_{\text{D}_n}(t) \mathrm d t$.
  
  + Doppler frequency shift $f_{\text{D}_n}(t)=v\cos(\theta(t))/\lambda$ with motion velocity $v$, angel of arrival relative to the direction of motion $\theta(t)$ and signal wavelength $\lambda$.
  
  + When $\phi_{\text{D}_n}(t)=0$, equations $\eqref{eq:ch_real}$ and $\eqref{eq:ch_complex}$ are equivalent (See $\eqref{eq:received_relation}$).

### Received signal

+ Transmitted signal (See [definition](#definition)): 

  + Real: $s(t)=s_\text{I}(t)\cos(2\pi f_\text{c}t)-s_\text{Q}(t)\cos(2\pi f_\text{c}t)$.

  + Complex baseband: $u(t)=s_\text{I}(t)+\mathrm{j}s_\text{Q}(t)$.

+ Received signal:

  + Real: 
    $$
    \begin{align}
    r(t) &= s(t) \otimes h_\text{real}(t,\tau) \nonumber \\
    &= s(t) \otimes \sum_{n=0}^{N(t)-1}\alpha_{n}(t)\delta(\tau-\tau_n(t)) \nonumber \\
    &=\sum_{n=0}^{N(t)-1}\alpha_{n}(t)s(t-\tau_n(t)).
    \label{eq:received_real}
    \end{align}
    $$
    
  + Complex baseband:
    $$
    \begin{align}
    u_r(t) &= u(t) \otimes h_\text{complex}(t,\tau)\nonumber \\
    &=u(t) \otimes \sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\mathrm{j}\phi_n(t))\delta(\tau-\tau_n(t)) \nonumber \\
    &=\sum_{n=0}^{N(t)-1}\alpha_n(t)u(t-\tau_n(t))\exp(-\mathrm{j}\phi_n(t)) \nonumber\\
    &=\sum_{n=0}^{N(t)-1}\alpha_n(t)u(t-\tau_n(t))\exp(-\mathrm{j}2\pi f_\text{c}\tau_n(t)+\phi_{\text{D}_n}(t)).
    \label{eq:received_complex}
    \end{align}
    $$
    
    Here, $\otimes$ denotes the convolution operation.
  
+ Relationship (using $\eqref{eq:complex2real}$): 
  $$
  \begin{align}
  r(t)&=\text{Re}\left\{u_r(t)\exp(\mathrm{j}2\pi f_\text{c}t)\right\} \nonumber \\
  &=\text{Re}\left\{\left[\sum_{n=0}^{N(t)-1}\alpha_n(t)u(t-\tau_n(t))\exp(-\mathrm{j}2\pi f_\text{c}\tau_n(t)+\phi_{\text{D}_n}(t))\right]\exp(\mathrm{j}2\pi f_\text{c}t)\right\} \nonumber \\
  &=\text{Re}\left\{\sum_{n=0}^{N(t)-1}\alpha_n(t)u(t-\tau_n(t))\exp(\mathrm{j}2\pi f_\text{c}(t-\tau_n(t))+\phi_{\text{D}_n}(t))\right\}.
  \end{align}
  $$
  Now consdiering zero doppler shift that $\phi_{\text{D}_n}(t)=0$, the upper equation could be further reduced as follows:
  $$
  \begin{align}
  &r(t)=\text{Re}\left\{\sum_{n=0}^{N(t)-1}\alpha_n(t)u(t-\tau_n(t))\exp(\mathrm{j}2\pi f_\text{c}(t-\tau_n(t)))\right\} \nonumber \\
  &=\text{Re}\left\{\sum_{n=0}^{N(t)-1}\alpha_n(t)[s_\text{I}(t-\tau_n(t))+\mathrm{j}s_\text{Q}(t-\tau_n(t))]\left[\cos(2\pi f_\text{c}(t-\tau_n(t)))+\mathrm{j}\sin(2\pi f_\text{c}(t-\tau_n(t))))\right]\right\} \nonumber \\
  &=\sum_{n=0}^{N(t)-1}\alpha_n(t)[s_\text{I}(t-\tau_n(t))\cos(2\pi f_\text{c}(t-\tau_n(t)))-s_\text{Q}(t-\tau_n(t))\sin(2\pi f_\text{c}(t-\tau_n(t)))] \nonumber\\
  &=\sum_{n=0}^{N(t)-1}\alpha_{n}(t)s(t-\tau_n(t)).
  \label{eq:received_relation}
  \end{align}
  $$
  

# Wideband / Narrowband Channel Model

### Narrowband Channel Model

~~To be updated (DDL: before 2023.10.18)...~~  (Updated at 2023.10.18)

When delay spread $T_\text{m}=\max_{i,j\in\{0,1,\ldots,N(t)-1\}}\{\tau_i-\tau_j\}$ and a manual signal period $T=1/B$ satisfies that $T_m \ll T$, we have $u(t-\tau_i)\approx u(t-\tau_0)\approx u(t)$. Equation $\eqref{eq:ch_complex}$ could be rewrote as:
$$
\begin{align}
h_\text{nb}(t,\tau)&\approx\sum_{n=0}^{N(t)-1}\alpha_n(t)\exp(-\mathrm{j}\phi_n(t))\delta(\tau-\tau_0).
\label{eq:ch_complex_nb}
\end{align}
$$
Moreover, received signal could be rewrote as:
$$
\begin{align}
u_r(t)&=u(t)\otimes h_\text{nb}(t,\tau) \nonumber \\
&=\sum_{n}^{N(t)-1}\alpha_n(t)u(t-\tau_0)\exp(-\mathrm{j}\phi_n(t)) \nonumber \\
&\approx	\sum_{n}^{N(t)-1}\alpha_n(t)u(t)\exp(-\mathrm{j}\phi_n(t))  \nonumber \\
&=u(t)\times \underbrace{\alpha_n(t)\exp(-\mathrm{j}\phi_n(t))}_{h_\text{nb}(t)}
\end{align}
$$
An interesting finding is that received signal $u_r(t)$ can be expressed as a multiplication of $u(t)$ and $h_\text{nb}(t)$ approximately at narrowband (No need of convolution!), and $h_\text{nb}(t)$ has similar expression with its CFR $H(t,f)$ in $\eqref{eq:CFR}$ if Doppler phase $\phi_{\text{D}_n} = 0$.

### Wideband Channel Model

**COMING SOON** (Computer science-ers' trash fake open-source style :sweat_smile:: To be updated in the infinite future... That's why i dont like them. If u can not make ur project public for some reason, it dosen't matter, but please do not cheat us and waste our time. Just a joke here.)

