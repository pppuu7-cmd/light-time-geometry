# EXP-043 — Cosmological photon zero-crossing and dark-energy branch test

## Objective

Test the hypothesis:

> Cosmological expansion stretches a photon until its measured energy reaches zero; continued geometric evolution then drives the photon onto a negative-energy branch, and that branch may behave as dark energy while the photon continues propagating outside our observable region.

## 1. Geometric redshift in FLRW

For spatially flat FLRW,

\[
ds^2=-dt^2+a(t)^2d\mathbf{x}^2.
\]

For a comoving observer \(u^\mu=(1,0,0,0)\),

\[
E=-p_\mu u^\mu.
\]

For a future-directed null geodesic with conserved comoving momentum magnitude \(q>0\),

\[
E(t)=\frac{q}{a(t)},
\qquad
\dot E=-HE.
\]

Therefore

\[
E(t)=E(t_i)\exp\!\left[-\int_{t_i}^{t}H(t')dt'\right].
\]

If \(E(t_i)>0\), then \(E(t)>0\) for every finite real integral. If \(a(t)\to\infty\), then \(E(t)\to0^+\), not through zero.

### Result 043A

\[
\boxed{\text{FLRW redshift alone cannot cause }E>0\to0\to E<0.}
\]

## 2. Negative photon-energy branch

For an isotropic massless ensemble,

\[
p_\gamma=\frac13\rho_\gamma,
\qquad
w_\gamma=\frac13.
\]

Even if a negative branch \(\rho_-<0\) is imposed,

\[
p_-=\frac13\rho_-,
\qquad
w_-=\frac13,
\]

and separate conservation gives

\[
\dot\rho_-+4H\rho_-=0,
\qquad
\rho_-\propto a^{-4}.
\]

A cosmological constant instead obeys

\[
p_\Lambda=-\rho_\Lambda,
\qquad
w_\Lambda=-1,
\qquad
\rho_\Lambda=\mathrm{const}.
\]

Thus a sign-flipped photon fluid is not vacuum dark energy.

The acceleration equation,

\[
\frac{\ddot a}{a}
=
-\frac{4\pi G}{3}\sum_i(\rho_i+3p_i),
\]

shows that negative radiation would formally contribute with an accelerating sign because \(\rho_-+3p_-=2\rho_-<0\), but its magnitude decays as \(a^{-4}\).

### Result 043B

A negative photon-like branch can formally accelerate, but it does not reproduce persistent late-time dark energy.

## 3. Horizon crossing

A cosmological horizon is a causal-accessibility boundary. For a future-directed photon and a future-directed local timelike observer,

\[
E_{\rm obs}=-p_\mu u^\mu>0.
\]

A photon becoming permanently unobservable to us does not imply a local zero or negative energy.

\[
\boxed{\text{horizon crossing}\not\Rightarrow\text{energy-sign reversal}.}
\]

## 4. Minimal conversion model

A distinct hypothesis is

\[
\gamma\longrightarrow X,
\]

where \(X\) is a new vacuum-like degree of freedom.

Use

\[
\dot\rho_\gamma+4H\rho_\gamma=-Q,
\]

\[
\dot\rho_X+3H(1+w_X)\rho_X=Q.
\]

For dark-energy-like behavior require \(w_X\simeq-1\).

For the phenomenological ansatz

\[
Q=\Gamma H\rho_\gamma,
\]

one gets

\[
\rho_\gamma(a)=
\rho_{\gamma,i}
\left(\frac{a}{a_i}\right)^{-(4+\Gamma)}.
\]

For \(w_X=-1\),

\[
\rho_X(a)=
\rho_{X,i}
+
\frac{\Gamma}{4+\Gamma}\rho_{\gamma,i}
\left[
1-\left(\frac{a}{a_i}\right)^{-(4+\Gamma)}
\right].
\]

This is mathematically consistent, but it requires a new interaction \(Q\), a distinct component \(X\), and its own equation of state.

## 5. Terminal classification

### Strict zero-crossing hypothesis

\[
\boxed{\text{geometry stretches an ordinary photon through }E=0\text{ into }E<0}
\]

**ANALYTIC FAIL in standard FLRW null-geodesic dynamics.**

### Negative-photon-dark-energy hypothesis

\[
\boxed{E_\gamma<0\Rightarrow\text{ordinary dark energy}}
\]

**FAIL as stated.**

### Conversion hypothesis

\[
\boxed{
\gamma
\stackrel{Q[g,\text{global causal data}]}{\longrightarrow}
X,
\qquad
w_X\simeq-1
}
\]

**MATHEMATICALLY OPEN.**

The next discriminating gate is whether geometry can derive a non-arbitrary \(Q^\mu\) rather than inserting it phenomenologically.
