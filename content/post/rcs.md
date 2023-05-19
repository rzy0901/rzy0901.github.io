---
title: "Notes for Bistatic Radar Cross Section (RCS)"
date: 2023-05-15T00:00:00+08:00
draft: true
tags: ["Math","Radar","RCS"]
categories: ["Math"]

contentCopyright: MIT
mathjax: true
autoCollapseToc: false
postMetaInFooter: true
reward: false
author: Ren Zhenyu
typora-copy-images-to: ../../static/rcs.assets
typora-root-url: ../../static
---

# Radar Cross Section

> This document records some possible useful rcs-related equations for my simulations :smile:.

## RCS Definition[^1]

The RCS represents an equivalent aperture surface area of the target, which captures a certain amount of incident radiation, and which, if re-radiated isotropically, would produce an equivalent scattered field at the receiver.

+ For 2d target:
  $$
  \begin{aligned}
  \sigma_{2d}=\begin{cases}\lim_\limits{\rho \to \infty}\left[2\pi \rho \frac{S^s}{S^i}\right]\\
  \lim_\limits{\rho \to \infty}\left[2\pi \rho \frac{|E^s|^2}{|E^i|^2}\right]\\
  \lim_\limits{\rho \to \infty}\left[2\pi \rho \frac{|H^s|^2}{|H^i|^2}\right]
  \end{cases}
  \end{aligned}.
  $$

+ For 3d target:
  $$
  \begin{aligned}
  \sigma_{3d}=\begin{cases}\lim_\limits{r \to \infty}\left[4\pi r^2 \frac{S^s}{S^i}\right]\\
  \lim_\limits{r \to \infty}\left[4\pi r^2 \frac{|E^s|^2}{|E^i|^2}\right]\\
  \lim_\limits{r \to \infty}\left[4\pi r^2 \frac{|H^s|^2}{|H^i|^2}\right]
  \end{cases}
  \end{aligned}.
  $$

+ Where $\rho,r=$ distance from target to observation point.

  + $S^s,S^i=$ scattered, incident power density.
  + $E^s,E^i$ = scattered, incident electric fields.
  + $H^s,H^i=$ scattered, incident magnetic fields.

## Monostatic and Bistatic RCS

Assuming a spherical coordinate system defined by $(\rho,\theta,\phi)$, denote the incident wave direction as $(\theta^i,\phi^i)$ and scattered wave direction as $(\theta_s,\phi_s)$.

+ RCS measured by $\theta_s=\theta_i$ and $\phi_s=\phi_i$ is called monostatic RCS (or backscattered RCS).
+ RCS measured by $\theta_s \neq \theta_i$ and $\phi_s \neq \phi_i$ is called bistatic RCS.

> Remark: In my opinion, monostatic RCS could be considered as a function of frequency and incident angles while bistatic RCS is more complex and can be considered as a function of frequency, incident angle, scattered angle, and bistatic angle.

## Monostatic to Bistatic Equivalence[^2]

Kell’s Monostatic-to-Bistatic Theorem[^3]
$$
\sigma_{bistatic}(\theta=\beta,f)=\sigma_{monostaic}(\theta=\beta/2,f \sec(\beta/2)).
$$
Crispin's Monostatic-to-Bistatic Equivalence Theorem[^4]:
$$
\sigma_{bistatic}(\theta=\beta,f)=\sigma_M(\theta=\beta/2,f).
$$
Here, $\beta$ refers to bistatic angle and $f$ refers to frequency.

## Bistatic RCS Estimation of an ellipsoid[^5] [^6]

> Reference[^6] corrects some mistakes of reference[^5].

<center><img src="/rcs.assets/image-20230515205823580.png" alt="image-20230515205823580" style="zoom:33%;" /></center>

Considering an ellipsoid with its center at the origin: 
$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1,
$$
where, $a$,$b$,$c$ represent the length of the three semi-axes of the ellipsoid in the $x$, $y$, $z$ directions respectively.

Denote the incident and scattered wave directions in spherical coordinate form as $(\theta_i,\phi_i)$ and $(\theta_s,\phi_s)$ respectively. Here, $\theta_i,\theta_s$ refer to the incident and scattered aspect angles while $\phi_i$, $\phi_s$ refer to the incident and scattered azimuth angles of the ellipsoid relative to the transmitter and receiver.

+ Then the bistatic RCS could be estimated by:

$$
\sigma_{bistatic} = \frac{4\pi a^2b^2c^2[(1+\cos \theta_i\cos\theta_s)\cos(\phi_s-\phi_i)+\sin\theta_i\sin\theta_s]^2}{\left[a^2(\sin\theta_i\cos\phi_i+\sin\theta_s\cos\phi_s)^2+b^2(\sin\theta_i\sin\phi_i+\sin\theta_s\sin\phi_s)^2+c^2(\cos\theta_i+\cos\theta_s)^2\right]^2}.
$$
+ For monostatic case ($\theta_i = \theta_s$, $\phi_i = \phi_s$), we have:

$$
\sigma_{monostatic}=\frac{\pi a^2b^2c^2}{[a^2\sin^2\theta_i\cos^2\phi_i+b^2\sin^2\theta_i\sin^2\phi_i+c^2\cos^2\theta]^2}.
$$

+ When $a=b=c=r$, we have rcs estimation of a sphere:
  $$
  \sigma_{monostatic-sphere}=\pi r^2.
  $$

## Radar Range Equation

+ Bistatic radar range equation:
  $$
  P_r=\frac{P_tG_tG_r\sigma_B\lambda^2}{(4\pi)^3R^2_{Tx}R^2_{Rx}}.
  $$

+ Monostatic radar range equation ($R_{Rx}=R_{Tx}=R$):
  $$
  P_{r}=\frac{P_{t}G_tG_r \sigma_{M} \lambda^2}{(4\pi)^3R^4}.
  $$
  Where:

  + $P_t$, $P_r$ refer to transmit and receive power.
  + $G_t$, $G_r$ refer to transmit and receive antenna gain.
  + $\sigma_B$ and $\sigma_M$ refer to bistatic and monostatic RCS.
  + $R_{Tx}$, $R_{Rx}$ refer to distance of transmitter-target and receiver-target.

[^1]:Balanis, Constantine A. *Advanced engineering electromagnetics*. John Wiley & Sons, 2012.
[^2]:Eigel Jr, Robert L. "Bistatic radar cross section (RCS) characterization of complex objects." (1999).
[^3]:Kell, Robert E., "On the Derivation of the Bistatic RCS from Monostatic Measurements," Proceedings of the IEEE. Vol XX No Y: 983-988, Aug 1965.
[^4]:Cispin, J. W. and Siegel, K. M. Methods of Radar Cross Section Analysis. New
[^5]:Radar Cross Section Handbook. United States, Plenum Press, 1970.
[^6]:K. D. Trott, "Stationary Phase Derivation for RCS of an Ellipsoid," in IEEE Antennas and Wireless Propagation Letters, vol. 6, pp. 240-243, 2007, doi: 10.1109/LAWP.2007.891521.
